from django.urls import path
from centroinvestigacion import views, views_enfoque
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views_enfoque.PaginaInicio.as_view(), name='bienvenida'),
    path('centros', views.ListaCentros.as_view(), name='centros_lista'),
    path('centro/nuevo', views.NuevoCentro.as_view(), name='nuevo_centro'),
    path('centro/editar/<int:pk>', views.EditarCentro.as_view(), name='editar_centro'),
    path('centro/eliminar/<int:pk>',
         views.EliminarCentro.as_view(), name='eliminar_centro'),
    path('centro/detalles/<int:id>', views.detalles_centros, name='detalles_centro'),
    

    path('enfoques', views_enfoque.ListaEnfoques.as_view(), name='enfoques_lista'),
    path('enfoques/nuevo', views_enfoque.NuevoEnfoqueView.as_view(),
         name='nuevo_enfoque'),
    path('enfoques/editar/<int:pk>',
         views_enfoque.EditarEnfoqueView.as_view(), name='editar_enfoque'),
    path('enfoques/eliminar/<int:pk>',
         views_enfoque.EliminarEnfoqueView.as_view(), name='eliminar_enfoque'),
]
