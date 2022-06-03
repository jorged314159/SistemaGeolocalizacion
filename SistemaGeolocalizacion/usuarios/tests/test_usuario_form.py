import unittest
from usuarios.forms import UserForm
from django.contrib.auth.models import User


class TestUserForm(unittest.TestCase):

    def setUp(self):

        self.user = User(
            username='herminio',
            password='jorgeRikudo',
            # repassword = 'jorgeRikudo',
            email='jorged314159@gmail.com'
        )

        self.data = {
            'username': 'herminio',
            'password': 'jorgeRikudo',
            'email': 'jorged314159@gmail.com',
            'repassword': 'jorgeRikudo'
        }

    # def loguearse(self):
    #     User.objects.create_user(
    #         username='herminio2',
    #         password='jorgeRikudo',
    #     )
    #     self.client.login(username='herminio2', password='jorgeRikudo')

    # def test_login_correcto(self):
    #     self.user.password('jorgeRikudo')
    #     self.user.save()
    #     self.loguearse()
    #     response = self.client.get('')
    #     self.assertEquals(response.status_code, 302)

    def test_usuario_form_valido(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'],
                         ['Este campo es obligatorio.'])

    def test_usuario_form_username_max_caracteres(self):
        self.data['username'] = 'a'*21
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'],
                         ['Asegúrese de que este valor tenga como máximo 20 caracteres (tiene 21).'])

    def test_usuario_form_email_invalido(self):
        self.data['email'] = 'omar_cruzrazo@hotmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], ['Este campo es obligatorio.'])

    def test_usuario_form_email_invalido_mensaje(self):
        self.data['email'] = 'omar_cruzrazo@hotmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], [
                         'Introduzca una dirección de correo electrónico válida.'])

    def test_usuario_form_password_vacio(self):
        self.data['password'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_vacio_mensaje(self):
        self.data['password'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], [
                         'Este campo es obligatorio.'])

    def test_usuario_form_password_invalido(self):
        self.data['password'] = 'alexdlcruz123'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_diferente_mensaje(self):
        self.data['password'] = 'alexdlcruz1'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'],
                         ['Las contraseñas son diferentes; favor de verificar'])

    def test_usuario_form_password_min_caracteres(self):
        self.data['password'] = 'alex'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_con_espacios(self):
        self.data['password'] = 'alex dlcruz'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_no_debe_tener_caracteres_especiales(self):
        self.data['password'] = 'alexdlcruz@'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_min_caracteres(self):
        self.data['username'] = 'alex'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
