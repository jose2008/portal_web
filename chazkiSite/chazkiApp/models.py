from django.db import models

# Create your models here.

class Persona(models.Model):
	'''Modelo de persona'''
	personaID = models.IntegerField(default = 0)
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	genero = models.CharField(max_length = 100)
	edad = models.IntegerField(default = 0)
	positionX = models.IntegerField(default = 0)
	positionY = models.IntegerField(default = 0)




class Vehiculo(models.Model):
	'''  Modelo de Vehiculo   '''
	vehiculoID = models.IntegerField(default = 0)
	placa = models.CharField(max_length = 100)
	cargaMudanza = models.BooleanField()
	portaBebe = models.BooleanField()
	portaAnimal = models.BooleanField()
	positionX = models.IntegerField(default = 0)
	positionY = models.IntegerField(default = 0)
