from django import forms
from django.contrib.auth.models import User
# from django.core.validators import MinLengthValidator


# class LoginForm(AuthenticationForm):

#     class Meta:
#         fields = '__all__'

#         witgets = {
#             'username' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'password' : forms.PasswordInput(attrs={'class' : 'form-control'})
#         }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repassword')

    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # Encripta la contraseña, no borrar
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['repassword']:
            raise forms.ValidationError(
                'Las contraseñas son diferentes; favor de verificar')
        return self.data['password']
