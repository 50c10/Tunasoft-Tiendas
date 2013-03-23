from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tienda.apps.ventas.views',
	url(r'^add/producto/$','add_producto_view',name='vista_agregar_producto'),
)