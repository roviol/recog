from django.db import models
from reconpath import settings

# Create your models here.
class ImgReferencia(models.Model):
	nombre =models.CharField(max_length = 255)
	imagen = models.ImageField(upload_to = 'imgref/', default = 'imgref/None/no-img.jpg')
	gris = models.ImageField(upload_to = 'gris/', default = 'gris/None/no-img.jpg')
	des = models.FileField(upload_to = 'des/', default = 'des/None/no-img.npy')
	def image_tag(self):
	    return u'<img width="640" src="/imgref/%s" />' % self.imagen
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True
	def __unicode__(self):
		return self.nombre

# Create your models here.
class ImgBusqueda(models.Model):
	nombre =models.CharField(max_length = 255)
	imagen = models.ImageField(upload_to = 'imgbusq/', default = 'imgbusq/None/no-img.jpg')
	gris = models.ImageField(upload_to = 'gris/', default = 'gris/None/no-img.jpg')
	des = models.FileField(upload_to = 'des/', default = 'des/None/no-img.npy')
	def image_tag(self):
	    return u'<img width="640" src="/imgref/%s" />' % self.imagen
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True
	def __unicode__(self):
		return self.nombre