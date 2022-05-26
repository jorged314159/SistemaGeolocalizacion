import unittest
from usuarios.forms import UserForm


class TestUserForm(unittest.TestCase):

    def setUp(self):
        
        self.data= {
            'username': 'alexdlcruz',
            'password': 'alexDlc123',
            'email': 'omar_cruzrazo@hotmail.com',
            'repasswpord' : 'alexDlc123'
        }

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
        self.assertEqual(form.errors['email'], ['Favor de ingresar un formato de correo válido.'])
        
    def test_usuario_form_password_vacio(self):
        self.data['password'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())
        
    def test_usuario_form_password_vacio_mensaje(self):
        self.data['password'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['Este campo es obligatorio.'])

    def test_usuario_form_password_invalido(self):
        self.data['password'] = 'alexdlcruz123'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_invalido_mensaje(self):
        self.data['password'] = 'alexdlcruz1'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['La contraseña debe tener al menos una mayúscula.'])
        
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
