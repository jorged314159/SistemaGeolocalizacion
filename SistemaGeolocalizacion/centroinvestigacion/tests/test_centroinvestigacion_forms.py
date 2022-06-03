import unittest
from centroinvestigacion.models import CentroInvestigacion, Enfoque
from centroinvestigacion.forms import FormCentroInvestigacion


class TestFormCentroInvestigacion(unittest.TestCase):

    def setUp(self):

        self.enfoque = Enfoque(
            nombre='Ciencias basicas',
            descripcion='Investigacion sobre las áreas de física, matemáticas y biología'
        )

        self.centro = CentroInvestigacion(
            nombre='Cozcyt',
            direccion='Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            latitud='22.7769839',
            longitud='-102.5719377',
            telefono='4922252720',
            enfoque=self.enfoque
        )

        self.data_Enfoque = {
            'nombre': 'Ciencias en General',
            'descripcion': 'Todo lo que se te ocurra'
        }

        self.data_Centro = {
            'nombre': 'Cozcyt',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': None
        }

    # Tests para centros de investigacion

    def test_centro_form_valido(self):
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertTrue(form.is_valid())

    def test_centro_form_nombre_vacio(self):
        self.data_Centro['nombre'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertFalse(form.is_valid())

    def test_centro_form_nombre_vacio_mensaje(self):
        self.data_Centro['nombre'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(
            form.errors['nombre'],
            ['Este campo es obligatorio.'])

    def test_centro_form_nombre_max_caracteres(self):
        self.data_Centro['nombre'] = 'a'*51
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(form.errors['nombre'], [
                         'Asegúrese de que este valor tenga como máximo 50 caracteres (tiene 51).'])

    def test_centro_form_nombre_duplicado(self):
        # self.centro.save()
        data_centro2 = {
            'nombre': 'Cozcyt',
            'direccion': 'Callejon IPN, S/N, Centro, 98000, Zacatecas2',
            'latitud': '22.78444282',
            'longitud': '-102.61190242',
            'telefono': '4929212812',
            'enfoque': self.enfoque
        }
        form = FormCentroInvestigacion(data=data_centro2)
        self.assertFalse(form.is_valid())

    def test_centro_form_direccion_vacia(self):
        self.data_Centro['direccion'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertFalse(form.is_valid())

    def test_centro_form_direccion_vacia_mensaje(self):
        self.data_Centro['direccion'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(
            form.errors['direccion'],
            ['Este campo es obligatorio.'])

    def test_centro_form_direccion_max_caracteres(self):
        self.data_Centro['direccion'] = 'a'*151
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(form.errors['direccion'], [
                         'Asegúrese de que este valor tenga' +
                         ' como máximo 150 caracteres (tiene 151).'])

    def test_centro_form_direccion_duplicada(self):
        # self.centro.save()
        data_centro2 = {
            'nombre': 'Cozcyt2',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.78444282',
            'longitud': '-102.61190242',
            'telefono': '4929212812',
            'enfoque': self.enfoque
        }
        form = FormCentroInvestigacion(data=data_centro2)
        self.assertFalse(form.is_valid())

    def test_centro_form_telefono_vacio(self):
        self.data_Centro['telefono'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertFalse(form.is_valid())

    def test_centro_form_telefono_vacia_mensaje(self):
        self.data_Centro['telefono'] = ''
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(
            form.errors['telefono'],
            ['Este campo es obligatorio.'])

    def test_centro_form_telefono_max_caracteres(self):
        self.data_Centro['telefono'] = '4'*11
        form = FormCentroInvestigacion(self.data_Centro)
        self.assertEqual(form.errors['telefono'], [
                         'Asegúrese de que este valor tenga como máximo 10 caracteres (tiene 11).'])

    def test_centro_form_telefono_duplicado(self):
        # self.centro.save()
        data_centro2 = {
            'nombre': 'Cozcyt2',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.78444282',
            'longitud': '-102.61190242',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        form = FormCentroInvestigacion(data=data_centro2)
        self.assertFalse(form.is_valid())
