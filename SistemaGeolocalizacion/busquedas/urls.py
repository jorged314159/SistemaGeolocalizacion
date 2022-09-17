from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from busquedas import views

urlpatterns = [
    path('', views.obtener_centros, name='obtener_centros'),
    # path('', views.buscar_municipio, name='buscar_municipio'),
    # path('', views.buscar_enfoque_area, name='buscar_enfoque_nombre'),
    # path('', views.buscar_enfoque_desc, name='buscar_enfoque_desc'),
]
