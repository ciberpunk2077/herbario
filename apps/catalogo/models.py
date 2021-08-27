import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.catalogo.extra import *

# Create your models here.

# Usuarios

class User(AbstractUser):
    administrador = models.BooleanField(default=False)
    capturista = models.BooleanField(default=False)
    usuario = models.BooleanField(default=False)



class Familia(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)

    class Meta:
        default_permissions =()


class Especie(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    familia = models.ForeignKey("catalogo.familia", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class Municipio(models.Model):
    clave = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    estado = models.PositiveSmallIntegerField(choices=ESTADOS, default=0)

    def __str__(self):
        return '{}-{} /{}'.format(self.clave, self.nombre, self.estado)


class Algas(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/algas/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'),  (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia", on_delete=models.CASCADE, null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class Planta(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/planta/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'), (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia",on_delete=models.CASCADE,null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class FrutoSemilla(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/frutosemilla/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'), (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia",on_delete=models.CASCADE,null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class Polen(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/polen/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'), (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia",on_delete=models.CASCADE,null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class Helecho(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/helecho/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'), (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia",on_delete=models.CASCADE,null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()

class Hongo(models.Model):

    def get_upload_path_imagen(instance, filename):
        folder = 'imagenes/hongo/{}/{}/{}'.format(instance.familia.nombre,instance.especie.nombre,instance.genero.nombre)
        ruta = os.path.join("media/",folder)
        return os.path.join(ruta,filename)

    genero = ((1, 'Masculino'), (2, 'Femenino'), (3, 'Hermafrodita'))

    nombre_cientifico = models.CharField(max_length=200)
    nombre_comun = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)
    numero_recolecta=models.IntegerField()
    colonia = models.CharField(max_length=200, null=True, blank=True)
    localidad = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    imagen = models.FileField(upload_to=get_upload_path_imagen, null=True, blank=True)
    familia = models.ForeignKey("catalogo.Familia",on_delete=models.CASCADE,null=True, blank=True)
    municipio = models.ForeignKey("catalogo.Municipio", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ()


