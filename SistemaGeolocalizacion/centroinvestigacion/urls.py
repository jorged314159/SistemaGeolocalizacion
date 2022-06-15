from django.urls import path
from centroinvestigacion import views, views_enfoque

urlpatterns = [
    path('', views_enfoque.PaginaInicio.as_view(), name='bienvenida'),
    path('centros', views.lista_centros, name='centros_lista'),
    path('centro/nuevo', views.nuevo_centro, name='nuevo_centro'),
    path('centro/editar/<int:id>', views.editar_centros, name='editar_centro'),
    path('centro/eliminar/<int:id>',
         views.eliminar_centros, name='eliminar_centro'),
    path('centro/detalles/<int:id>', views.detalles_centros, name='detalles_centro'),
    

    path('enfoques', views_enfoque.ListaEnfoques.as_view(), name='enfoques_lista'),
    path('enfoques/nuevo', views_enfoque.NuevoEnfoqueView.as_view(),
         name='nuevo_enfoque'),
    path('enfoques/editar/<int:pk>',
         views_enfoque.EditarEnfoqueView.as_view(), name='editar_enfoque'),
    path('enfoques/eliminar/<int:pk>',
         views_enfoque.EliminarEnfoqueView.as_view(), name='eliminar_enfoque'),
]
