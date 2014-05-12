from django.db import models
from tienda.apps.subdomains.models import Subdomain
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your models here.

class propiedades(models.Model):
	color_fondo = models.CharField(max_length=10)
	logo 		= models.CharField(max_length=10)
	layout		= models.CharField(max_length=10)

	def __unicode__(self):
		return self.layout

class tienda(models.Model):
	subdomain = models.ForeignKey(Subdomain)
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	propiedades = models.ForeignKey(propiedades)
	
	def __unicode__(self):
		return self.nombre

class cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos =models.CharField(max_length=200)
	status = models.BooleanField(default=True)

	def __unicode__ (self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto


class categoria(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion =models.CharField(max_length=200)
	tienda = models.ForeignKey(tienda)

	def __unicode__(self):
		return self.nombre

class imagen(models.Model):
    image = models.ImageField(upload_to ="photos/originals/%Y/%m/")
   
class producto(models.Model):
	nombre = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=7,decimal_places=2)
	stock = models.IntegerField(default = 0)
	descripcion = models.TextField(max_length=300)
	status = models.BooleanField(default=True)
	tienda = models.ForeignKey(tienda)
	imagenes = models.ManyToManyField(imagen)
	categoria = models.ManyToManyField(categoria,null=True,blank=True)

	def __unicode__(self):
		return self.nombre
