import unittest
from centroinvestigacion.models import CentroInvestigacion, Enfoque
from django.core.exceptions import ValidationError


class TestCentrosInvestigacionModels(unittest.TestCase):
    
    
    
    def setUp(self):
        
        self.enfoque = Enfoque(
            nombre = 'Ciencias básicas',
            descripcion = 'Investigacion sobre las áreas de física, matemáticas y biología'
        )
        
        self.centro = CentroInvestigacion(
                nombre = 'Cozcyt',
                direccion = 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
                latitud = '22.7769839',
                longitud = '-102.5719377',
                telefono = '4922252720',
                enfoque = self.enfoque
        )
        
        
    # Pruebas para el model Centro de Investigación
       
    def test_nombre_es_requerido(self):
        centro = CentroInvestigacion(
            direccion = 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            latitud = '22.7769839',
            longitud = '-102.5719377',
            telefono = '4922252720',
            enfoque = self.enfoque
        )
        with self.assertRaises(ValidationError):
            centro.full_clean()
            
    def test_nombre_max_50_caracteres(self):
        self.centro.nombre = 'c'*51
        with self.assertRaises(ValidationError):
            self.centro.full_clean()
            
    def test_nombre_centro_duplicado(self):
        centro2 = CentroInvestigacion(
            nombre = 'Cozcyt',
            direccion = 'Av. Hidalgo, #673, Centro, 98000, Zacatecas',
            latitud = '23.7769839',
            longitud = '-100.5719377',
            telefono = '4921234567',
            enfoque = self.enfoque

        )
        try:
            centro2.full_clean()
        except ValidationError as ve:
            mensaje = str(ve.message_dict['nombre'][0])
            self.assertEqual(mensaje, 'Ya existe un/a Centro investigacion con este/a Nombre.')
            
    def test_direccion_es_requerida(self):
        centro = CentroInvestigacion(
            nombre = 'Cozcyt',
            latitud = '22.7769839',
            longitud = '-102.5719377',
            telefono = '4922252720',
            enfoque = self.enfoque
        )
        with self.assertRaises(ValidationError):
            centro.full_clean()
        
    def test_direccion_max_150_caracteres(self):
        self.centro.nombre = 'a'*151
        with self.assertRaises(ValidationError):
            self.centro.full_clean()
            
    def test_direccion_centro_duplicada(self):
        centro2 = CentroInvestigacion(
            nombre = 'Quantum',
            direccion = 'Av. Hidalgo, #673, Centro, 98000, Zacatecas',
            latitud = '27.7769839',
            longitud = '-101.5719377',
            telefono = '4924234567',
            enfoque = self.enfoque
        )
        try:
            centro2.full_clean()
        except ValidationError as ve:
            mensaje = str(ve.message_dict['direccion'][0])
            self.assertEqual(mensaje, 'Ya existe un/a Centro investigacion con este/a Direccion.')
            
    def test_telefono_es_requerido(self):
        centro = CentroInvestigacion(
            nombre = 'Cozcyt',
            direccion = 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            latitud = '22.7769839',
            longitud = '-102.5719377',
            enfoque = self.enfoque
        )
        with self.assertRaises(ValidationError):
            centro.full_clean()
        
    def test_telefono_max_10_caracteres(self):
        self.centro.telefono = '4'*11
        with self.assertRaises(ValidationError):
            self.centro.full_clean()
            
    def test_telefono_centro_duplicado(self):
        centro2 = CentroInvestigacion(
            nombre = 'Quantum2',
            direccion = 'Av. Hidalgo, #673, Centro, 98000, Zacatecas2',
            latitud = '29.7769839',
            longitud = '-105.5719377',
            telefono = '4922252720',
            enfoque = self.enfoque
        )
        try:
            centro2.full_clean()
        except ValidationError as ve:
            mensaje = str(ve.message_dict['telefono'][0])
            self.assertEqual(mensaje, 'Ya existe un/a Centro investigacion con este/a Telefono.')
    
    def test_latitud_es_requerida(self):
        centro = CentroInvestigacion(
            nombre = 'Cozcyt2',
            direccion = 'Av. Hidalgo, #723, Centro, 98000, Zacatecas2',
            longitud = '-102.5719377',
            telefono = '4922252720',
            enfoque = self.enfoque
        )
        with self.assertRaises(ValidationError):
            centro.full_clean()

    def test_longitud_es_requerida(self):
        centro = CentroInvestigacion(
            nombre = 'Cozcyt2',
            direccion = 'Av. Hidalgo, #723, Centro, 98000, Zacatecas2',
            latitud = '29.7769839',
            telefono = '4922252720',
            enfoque = self.enfoque
        )
        with self.assertRaises(ValidationError):
            centro.full_clean()
    
    def test_latitud_y_longitud_duplicados(self):
        centro2 = CentroInvestigacion(
            nombre = 'Quantum',
            direccion = 'Av. Hidalgo, #673, Centro, 98000, Zacatecas2',
            latitud = '22.7769839',
            longitud = '-102.5719377',
            telefono = '4924234567',
            enfoque = self.enfoque
        )
        try:
            centro2.full_clean()
        except ValidationError as ve:
            mensaje = str(ve.message_dict['latitud'][0])
            mensaje2 = str(ve.message_dict['longitud'][0])
            self.assertEqual(mensaje, 'Ya existe un/a Centro investigacion con este/a Latitud.')
            self.assertEqual(mensaje2, 'Ya existe un/a Centro investigacion con este/a Longitud.')
    
    
    # Pruebas para el modelo de Enfoque
    
    def test_nombre_modelo_es_requerido(self):
        enfoque = Enfoque()
        
        with self.assertRaises(ValidationError):
            enfoque.full_clean()
    
    def test_nombre_enfoque_duplicado(self):
        enfoque2 = Enfoque(
            nombre = "Ciencias de la Computacion"
        )
        try:
            enfoque2.full_clean()
        except ValidationError as ve:
            mensaje = str(ve.message_dict['nombre'][0])
            self.assertEqual(mensaje, 'Ya existe un/a Enfoque con este/a Nombre.')