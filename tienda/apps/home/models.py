from django.db import models
from django.contrib.auth.models import User
from tienda.apps.ventas.models import tienda
# Create your models here.


class userProfile(models.Model):
	user = models.OneToOneField(User)
	tienda = models.ForeignKey(tienda)
	
	def __unicode__(self):
		return self.user.username
