from django.db import models
from App_tienda.models import *


# Create your models here.
class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=150)

class Seccion(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
   


    

