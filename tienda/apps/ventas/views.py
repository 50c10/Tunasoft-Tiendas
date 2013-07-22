# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from tienda.apps.ventas.forms import addProductForm
from tienda.apps.ventas.models import producto
from django.http import HttpResponseRedirect

def add_producto_view(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST)
			info = "inicializando"
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				p = producto()
				p.nombre = nombre
				p.descripcion = descripcion
				p.status = True
				p.save()
				info = "ya se guardo la mamada"
			else:
				info = "esta madre esta mal"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))
		else:
			form = addProductForm()
			ctx = {'form':form}
			return render_to_response('ventas/addproducto.html',ctx, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')

def dashboard_view(request):
	tienda = request.user.get_profile().tienda
	nombre_tienda = tienda.nombre
	ctx = {'nombre_tienda':nombre_tienda}
	return render_to_response('ventas/dashboard.html',ctx, context_instance=RequestContext(request))