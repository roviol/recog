from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reconpath.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/$', 'reconloc.views.upload_pic', name='upload_pic'),
    url(r'^compara/$', 'reconloc.views.compara', name='compara'),
    url(r'^imagen/$', 'reconloc.views.imagen', name='imagen'),
    url(r'^comparar/$', 'reconloc.views.comparar', name='comparar'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
