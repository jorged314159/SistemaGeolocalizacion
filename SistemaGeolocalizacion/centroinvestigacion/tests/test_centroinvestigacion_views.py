from django.test import TestCase
from django.contrib.auth.models import User
from centroinvestigacion.models import CentroInvestigacion, Enfoque


class TestViewsCentroInvestigacion(TestCase):

    def setUp(self):

        self.usuario = User(
            username='jorgeluis',
            email='30114724@uaz.edu.mx',
            password='jorgeRikudo',
            is_superuser=True,
            is_active=True
        )

        self.enfoque = Enfoque(
            nombre='Ciencias basicas',
            descripcion='Investigacion sobre las áreas de física, matemáticas y biología'
        )

        self.centro = CentroInvestigacion(
            nombre='MIMAZ',
            direccion='Paseo la Bufa, S/N, Av. Solidaridad, 98060, Zacatecas',
            latitud='22.7704422',
            longitud='-102.5604919',
            telefono='4929229975',
            enfoque=None
        )

        self.data_Centro = {
            'nombre': 'Cozcyt',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }

    def insertaCentro(self):

        self.enfoque = Enfoque(
            nombre='Ciencias Sociales',
            descripcion='Hacen cosas sobre la sociedad'
        )
        self.enfoque.save()

        self.centro = CentroInvestigacion(
            nombre='MIMAZ',
            direccion='Paseo la Bufa, S/N, Av. Solidaridad, 98060, Zacatecas',
            latitud='22.7704422',
            longitud='-102.5604919',
            telefono='4929229975',
            enfoque=self.enfoque
        )
        self.centro.save()
        return self.centro

    def test_ver_lista_centros_investigacion(self):
        self.loguearse()
        # self.insertaCentro()
        response = self.client.get('/centros')
        # print(response)
        self.assertEqual(response.status_code, 200)

    def test_guardar_centro_y_redirige_a_lista_centros(self):
        self.loguearse()
        self.client.get('/centro/nuevo', data=self.data_Centro)
        # self.insertaCentro()
        response = self.client.get('/centros')
        self.assertEqual(response.status_code, 200)

    def test_crear_nuevo_centro(self):
        self.loguearse()
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.insertaCentro()
        self.assertEqual(CentroInvestigacion.objects.all().count(), 1)

    def test_insertar_centro_y_redirige_a_lista_centros(self):
        self.loguearse()
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.insertaCentro()
        response = self.client.get('/centros')
        self.assertEqual(response.status_code, 200)

    def test_no_agrega_centro_sin_nombre(self):
        self.loguearse()
        self.data_Centro['nombre'] = ''
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_nombre_centro_duplicado(self):
        self.data_Centro2 = {
            'nombre': 'Cozcyt2',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        self.loguearse()
        self.client.post('/centro/nuevo', data=self.data_Centro2)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_no_agrega_centro_sin_direccion(self):
        self.loguearse()
        self.data_Centro['direccion'] = ''
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_direccion_centro_duplicado(self):
        self.data_Centro2 = {
            'nombre': 'Ayudame jesus',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        self.loguearse()
        self.client.post('/centro/nuevo', data=self.data_Centro2)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_nombre_centro_max_caracteres(self):
        self.loguearse()
        self.data_Centro['nombre'] = 'a'*51
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_direcion_centro_max_caracteres(self):
        self.loguearse()
        self.data_Centro['direccion'] = 'a'*151
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_direcion_centro_min_caracteres(self):
        self.loguearse()
        self.data_Centro['direccion'] = 'a'*19
        self.client.post('/centro/nuevo', data=self.data_Centro)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def test_editar_nombre_centro_correctamente(self):
        self.data_Centro2 = {
            'nombre': 'Cozcyt',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        self.loguearse()
        centro = self.insertaCentro()
        self.client.post('/centro/editar/' + str(centro.id),
                         data=self.data_Centro2)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 1)

    def test_editar_nombre_centro_y_redirige_a_lista_centros(self):
        self.data_Centro2 = {
            'nombre': 'Cozcyt',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        self.loguearse()
        centro = self.insertaCentro()
        self.client.get('/centro/editar/' + str(centro.id),
                        data=self.data_Centro2)
        response = self.client.get('/centros')
        self.assertEqual(response.status_code, 200)

    def test_editar_nombre_centro_incorrectamente(self):
        self.data_Centro2 = {
            'nombre': 'Cozcyt',
            'direccion': 'Av. Hidalgo, #723, Centro, 98000, Zacatecas',
            'latitud': '22.7769839',
            'longitud': '-102.5719377',
            'telefono': '4922252720',
            'enfoque': self.enfoque
        }
        self.loguearse()
        centro = self.insertaCentro()
        self.client.post('/centro/editar/' + str(centro.id),
                         data=self.data_Centro2)
        self.assertEqual(CentroInvestigacion.objects.first().nombre, 'MIMAZ')

    def test_eliminar_centro_correctamente(self):
        self.loguearse()
        centro = self.insertaCentro()
        # print(CentroInvestigacion.objects.all())
        self.client.get('/centro/eliminar/' + str(centro.id))
        # print(response)
        self.assertEqual(CentroInvestigacion.objects.all().count(), 0)

    def loguearse(self):
        User.objects.create_user(
            username='jorgeD',
            password='jorgeRikudo',
            email='jorged314159@gmail.com',
            is_staff=True
        )
        self.client.login(username='jorgeD', password='jorgeRikudo')
