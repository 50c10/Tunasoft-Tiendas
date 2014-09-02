from django.conf.urls import patterns,url

urlpatterns = patterns('tienda.apps.ventas.views',
	url(r'^add/producto/$','add_producto_view',name='vista_agregar_producto'),
	url(r'^dashboard/$','dashboard_view',name='vista_dashboard'),
	url(r'^ordenes/$','ordenes_view',name='vista_ordenes'),
	url(r'^productos/$','productos_view',name='vista_productos'),
	url(r'^producto/(?P<id_producto>.*)/$','producto_view',name='vista_producto'),
	url(r'^add/categoria/$','add_categoria_view',name='vista_agregar_categoria'),
	url(r'^categorias/$','categorias_view',name='vista_categorias'),
	url(r'^configuracion/$','configuracion_tienda_view',name='vista_configuracion_tienda'),
	url(r'^herramienta/$','herramienta_view',name='vista_herramienta'),
	url(r'^conf-envios/$','confEnvios_view',name='vista_conf-envios'),
	url(r'^show/$','show',name='show'),
	url(r'^add/$', 'add', name='add'),
	url(r'^addCart/$', 'addCart', name='addCart'),
)