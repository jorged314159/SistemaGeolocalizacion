from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# from .forms import LoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse_lazy



class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    # form_class = LoginForm

class RegistrarView(CreateView):
    template_name = 'user_form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
