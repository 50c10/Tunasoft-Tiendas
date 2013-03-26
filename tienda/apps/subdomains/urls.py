
from django.conf.urls.defaults import *

urlpatterns = patterns('tienda.apps.subdomains.views',
    url(r'^registro/$', 'create_subdomain', name='registro'),
)

