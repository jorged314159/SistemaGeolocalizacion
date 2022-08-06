from django.urls import path
from busquedas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.buscar_nombre, name='buscar_nombre'),
    path('', views.buscar_municipio, name='buscar_municipio'),
    path('', views.buscar_enfoque_nombre, name='buscar_enfoque_nombre'),
    path('', views.buscar_enfoque_desc, name='buscar_enfoque_desc'),
]
