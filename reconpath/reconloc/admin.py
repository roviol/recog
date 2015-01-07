from django.contrib import admin
from reconloc.models import ImgReferencia

class ImgReferenciaAdmin(admin.ModelAdmin):
	readonly_fields = ('image_tag',)


admin.site.register(ImgReferencia, ImgReferenciaAdmin)