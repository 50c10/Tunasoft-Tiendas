# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from tienda.apps.ventas.forms import addProductForm
from tienda.apps.ventas.models import producto
from django.http import HttpResponseRedirect

def add_producto_view(request):
	if request.user.is_authenticated():
		tienda_actual = request.user.get_profile().tienda
		if request.method == "POST":
			form = addProductForm(request.POST)
			info = "inicializando"
			alert = "ini"
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				p = producto()
				p.nombre = nombre
				p.descripcion = descripcion
				p.status = True
				p.tienda = tienda_actual
				p.save()
				alert = "suc"
				info = "El producto %s se guardo con exito" % (p.nombre)
			else:
				alert = "war"
				info = "esta madre esta mal"
			form = addProductForm()
			ctx = {'form':form, 'informacion':info, 'alert':alert}
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

def ordenes_view(request):
	return render_to_response('ventas/ordenes.html',context_instance=RequestContext(request))

def productos_view(request):
	tienda_actual = request.user.get_profile().tienda
	prod = producto.objects.filter(status=True).filter(tienda=tienda_actual)
	return render(request,'ventas/productos.html',{'productos':prod})

def categorias_view(request):
	return render_to_response('ventas/categorias.html',context_instance=RequestContext(request))

def add_categoria_view(request):
	return render_to_response('ventas/addcategoria.html', context_instance=RequestContext(request))

def configuracion_tienda_view(request):
	return render(request,'ventas/configtienda.html')

def herramienta_view(request):
	return render(request,'ventas/herramientadiseno.html')

def confEnvios_view(request):
	return render(request,'ventas/conf-envios.html')