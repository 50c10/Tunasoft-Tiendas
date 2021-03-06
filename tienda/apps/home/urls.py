from django.conf.urls import patterns,url

urlpatterns = patterns('tienda.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^planes/$','planes_view',name='vista_planes'),
	url(r'^beneficios/$','beneficios_view',name='vista_beneficios'),
	url(r'^ayuda/$','ayuda_view',name='vista_ayuda'),

#Urls para el login/logout
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),	

#urls para el registro de tiendas
	url(r'^registro/$','registro_view',name='vista_registro'),


)
