
from django.conf.urls.defaults import *

urlpatterns = patterns('tienda.apps.subdomains.views',
    url(r'^create/subdomain/$', 'create_subdomain', name='subdomains_create_subdomain'),
)

