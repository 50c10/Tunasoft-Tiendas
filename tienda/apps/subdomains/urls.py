
from django.conf.urls import *

urlpatterns = patterns('tienda.apps.subdomains.views',
    url(r'^subdomain/$', 'create_subdomain', name='subdomain'),
    #url(r'^registro/$', 'registro', name='registro'),
)

