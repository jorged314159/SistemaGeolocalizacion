from django.db import models

# Create your models here.

class CentroInvestigacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField('Direccion', max_length=150, unique=True)
    latitud = models.CharField(max_length=20, unique=True)
    longitud = models.CharField(max_length=20, unique=True)
    telefono = models.CharField('Telefono', max_length=10, unique=True)
    #Pinche jorge pendejo
    
    def __str__(self):
        return self.nombre 