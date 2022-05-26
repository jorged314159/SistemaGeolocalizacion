from dataclasses import fields
from re import template
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
# from django.core.validators import MinLengthValidator
from django.core import validators


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
    password = forms.CharField(validators=[validators.MinLengthValidator(8, 'password')])
    repassword = forms.CharField(validators=[validators.MinLengthValidator(8, 'repassword')])

    
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['repassword']:
            raise forms.ValidationError('Las contraseñas son diferentes; favor de verificar')
        return self.data['password']
