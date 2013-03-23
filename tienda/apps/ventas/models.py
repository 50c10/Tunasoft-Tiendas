from django.db import models
from tienda.apps.subdomains.models import Subdomain	

# Create your models here.
class tienda(models.Model):
	subdomain = models.ForeignKey(Subdomain)
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)

class cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos =models.CharField(max_length=200)
	status = models.BooleanField(default=True)

	def __unicode__ (self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto


class producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre