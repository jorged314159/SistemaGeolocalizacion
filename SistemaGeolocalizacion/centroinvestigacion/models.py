from django.db import models


class CentroInvestigacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True, blank=False)
    calle = models.CharField(
        'Calle', max_length=150, null=False, blank=False)
    colonia = models.CharField(
        'Colonia', max_length=150, null=False, blank=False)
    numExterior = models.CharField(
        'Numero Exterior', max_length=5, null=False, blank=False)
    cp = models.CharField(
        'Codigo Postal', max_length=5, null=False, blank=False)
    estado = models.CharField(
        'Estado', max_length=150, null=False, blank=False)
    municipio = models.ForeignKey("centroinvestigacion.Municipio", verbose_name="Municipio",
        on_delete=models.DO_NOTHING, null=False, blank=False)
    latitud = models.CharField(max_length=20, unique=True, blank=False)
    longitud = models.CharField(max_length=20, unique=True, blank=False)
    telefono = models.CharField(
        'Telefono', max_length=10, unique=True, blank=False)
    areaEnfoque = models.ForeignKey("centroinvestigacion.Area", verbose_name="Area",
                                on_delete=models.DO_NOTHING, null=False, blank=False)
    subAreaEnfoque = models.ForeignKey("centroinvestigacion.Enfoque", verbose_name="Subarea",
                                on_delete=models.DO_NOTHING, null=False, blank=False)
    sitioWeb = models.CharField(max_length=100, unique=True, blank=True)
    imagen = models.ImageField(null = True, blank = True, upload_to = 'foto/')
    logotipo = models.ImageField(null = True, blank = True, upload_to = 'logos/')
    nombreEncargado = models.CharField('Nombre',max_length=100, unique=True, blank=False)
    correoEncargado = models.CharField('Correo',max_length=50, unique=True, blank=False)
    telefonoEncargado = models.CharField('Teléfono',max_length=10, unique=True, blank=False)


    def __str__(self):
        return self.nombre

class Enfoque(models.Model):
    area = models.ForeignKey("centroinvestigacion.Area", verbose_name="Area",
                                on_delete=models.DO_NOTHING, null=False, blank=False)
    subarea = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    descripcion = models.CharField(
        'Descripción', null=False, blank=False, max_length=150)

    def __str__(self):
        return self.subarea

class Area(models.Model):
    nombre = models.CharField(
        max_length=150, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=150, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nombre