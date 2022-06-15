from django.db import models


class CentroInvestigacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True, blank=False)
    direccion = models.CharField(
        'Direccion', max_length=150, unique=True, blank=False)
    latitud = models.CharField(max_length=20, unique=True, blank=False)
    longitud = models.CharField(max_length=20, unique=True, blank=False)
    telefono = models.CharField(
        'Telefono', max_length=10, unique=True, blank=False)
    enfoque = models.ForeignKey("centroinvestigacion.Enfoque", verbose_name="Enfoque",
                                on_delete=models.DO_NOTHING, null=True, blank=True)
    sitioWeb = models.CharField(max_length=100, unique=True, blank=True)
    imagen = models.ImageField(null = True, blank = True, upload_to = 'foto/')
    

    def __str__(self):
        return self.nombre


class Enfoque(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    descripcion = models.CharField(
        'Descripción', null=False, blank=False, max_length=150)

    def __str__(self):
        return self.nombre
