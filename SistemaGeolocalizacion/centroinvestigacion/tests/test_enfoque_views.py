from django.test import TestCase
from django.contrib.auth.models import User
from centroinvestigacion.models import Enfoque


class TestViewsEnfoque(TestCase):

    def setUp(self):

        self.data_Enfoque = {
            'nombre': 'Ciencias de la computacion',
            'descripcion': 'Hacen cosas de hackers'
        }

    def test_ver_lista_enfoques(self):
        self.loguearse()
        response = self.client.get('/enfoques')
        self.assertEqual(response.status_code, 200)

    def test_crear_nuevo_enfoque(self):
        self.loguearse()
        self.client.post('/enfoques/nuevo', data=self.data_Enfoque)
        # self.insertarEnfoque()
        # print(Enfoque.objects.all())
        self.assertEqual(Enfoque.objects.all().count(), 1)

    def test_no_agrega_enfoque_sin_nombre(self):
        self.loguearse()
        self.data_Enfoque['nombre'] = ''
        self.client.post('/enfoques/nuevo', data=self.data_Enfoque)
        self.assertEqual(Enfoque.objects.all().count(), 0)

    def test_nombre_enfoque_duplicado(self):
        self.data_Enfoque2 = {
            'nombre': 'Ciencias Sociales',
            'descripcion': 'Hacen cosas de hackers'
        }
        self.loguearse()
        self.insertarEnfoque()
        self.client.post('/enfoques/nuevo', data=self.data_Enfoque2)
        self.assertEqual(Enfoque.objects.all().count(), 1)

    def test_modifica_nombre_enfoque(self):
        self.data_Enfoque2 = {
            'nombre': 'Ciencias basicas',
            'descripcion': 'pos hace cosas basicas'
        }
        self.loguearse()
        enfoque = self.insertarEnfoque()
        self.client.post('/enfoques/editar/' + str(enfoque.id),
                         data=self.data_Enfoque2)
        response = self.client.get('/enfoques')
        self.assertEqual(response.status_code, 200)

    def test_modifica_nombre_enfoque_incorrectamente(self):
        self.data_Enfoque2 = {
            'nombre': '',
            'descripcion': 'pos hace cosas saludables'
        }
        self.loguearse()
        enfoque = self.insertarEnfoque()
        self.client.post('/enfoques/editar/' + str(enfoque.id),
                         data=self.data_Enfoque2)
        # print(Enfoque.objects.first())
        self.assertEqual(Enfoque.objects.first().nombre, 'Ciencias Sociales')

    def test_elimina_enfoque_correctamente(self):
        self.loguearse()
        enfoque = self.insertarEnfoque()
        self.client.post('/enfoques/eliminar/' + str(enfoque.id))
        response = self.client.get('/enfoques')
        self.assertEqual(response.status_code, 200)

    def loguearse(self):
        User.objects.create_user(
            username='jorgeD',
            password='jorgeRikudo',
            email='jorged314159@gmail.com',
            is_staff=True
        )
        self.client.login(username='jorgeD', password='jorgeRikudo')

    def insertarEnfoque(self):
        self.enfoque = Enfoque(
            nombre='Ciencias Sociales',
            descripcion='Hacen cosas sobre la sociedad xD'
        )
        self.enfoque.save()
        return self.enfoque
