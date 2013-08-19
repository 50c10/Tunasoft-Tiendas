# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from tienda.apps.ventas.models import producto, tienda, propiedades
from tienda.apps.subdomains.models import Subdomain
from tienda.apps.subdomains.middleware import get_current_subdomain
from tienda.apps.home.forms import ContactoForm, LoginForm, RegistroForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from tienda.apps.home.models import userProfile

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django import forms

def index_view(request):
	subdomain = get_current_subdomain()
	if subdomain == None:
		return render_to_response('bienvenida.html', context_instance=RequestContext(request))
	else:
		tienda_actual = tienda.objects.get(subdomain=subdomain)
		nombre_tienda = tienda_actual.nombre
		prod = producto.objects.filter(status=True).filter(tienda=tienda_actual)
		color_fondo = tienda_actual.propiedades.color_fondo
		ctx = {'productos':prod, 'nombre_tienda':nombre_tienda , 'color_fondo':color_fondo}
		return render_to_response('home/index.html',ctx, context_instance=RequestContext(request))

def registro_view(request):
	reguistro_correcto	= False
	usuario 			= ""
	Email 				= ""
	password 			= ""
	password2 			= ""
	nombre_tienda 		= ""

	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			reguistro_correcto = True
			usuario = form.cleaned_data['usuario']
			Email = form.cleaned_data['Email']
			password = form.cleaned_data['password']
			nombre_tienda = form.cleaned_data['tienda']
			password2 = form.cleaned_data['password2']

			usuario = User.objects.create_user(usuario,Email,password)
			usuarioProfile = userProfile()

			pTienda = propiedades()
			pTienda.color_fondo = '#888'
			pTienda.logo = nombre_tienda
			pTienda.layout = nombre_tienda
			pTienda.save()

			tiendao = tienda()
			tiendao.nombre = nombre_tienda
			tiendao.propiedades = pTienda
			tiendao.subdomain = Subdomain.objects.register_new_subdomain(subdomain_text = nombre_tienda, name=nombre_tienda, description = nombre_tienda, user = usuario)
			tiendao.save()
			usuarioProfile.tienda = tiendao
			usuarioProfile.user = usuario
			usuarioProfile.save()
	else :
		form = RegistroForm()
	ctx = {'form':form,'reguistro_correcto':reguistro_correcto}
	return render_to_response('home/registro.html',ctx,context_instance=RequestContext(request))

def about_view(request):
	mensaje = "Esto es un mensaje desde mi vista"
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html', ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False 
	email =""
	titulo = ""
	texto = ""

	if request.method == "POST":
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# COnfiguraciond de envio de correo

			to_admin = 'pako50c10@gmail.com'
			html_content = "Informacion recibida <br><br><br>Mensaje<br><br><br>%s"%(texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		formulario = ContactoForm()
	ctx = {'form':formulario, 'email':email, 'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx, context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/dashboard/')
				else:
					mensaje = "usuario o password incorrecto"
		form = LoginForm()
		ctx ={'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
