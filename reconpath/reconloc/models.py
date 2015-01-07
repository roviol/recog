from django.db import models
from reconpath import settings

# Create your models here.
class ImgReferencia(models.Model):
	imagen = models.ImageField(upload_to = 'imgref/', default = 'imgref/None/no-img.jpg')
	def image_tag(self):
	    return u'<img width="640" src="/imgref/%s" />' % self.imagen
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True