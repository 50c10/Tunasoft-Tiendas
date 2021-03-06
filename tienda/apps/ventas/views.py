# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from tienda.apps.ventas.forms import addProductForm, addCategoriaForm, addCartForm
from tienda.apps.ventas.models import producto , categoria
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from carton.cart import Cart

def add_producto_view(request):
	if request.user.is_authenticated():
		tienda_actual = request.user.get_profile().tienda
		if request.method == "POST":
			form = addProductForm(request.POST,request.FILES)
			info = "inicializado"
			alert = "ini"
			if form.is_valid:
				add = form.save(commit=False)
				add.status = True
				add.tienda = tienda_actual
				add.save()
				form.save_m2m()
				alert = "suc"
				info = "El producto %s se guardo con exito" % (add.nombre)
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

def add_categoria_view(request):
	if request.user.is_authenticated():
		tienda_actual = request.user.get_profile().tienda
		if request.method == "POST":
			form = addCategoriaForm(request.POST,request.FILES)
			info = "inicializado"
			alert = "ini"
			if form.is_valid:
				add = form.save(commit=False)
				add.tienda = tienda_actual
				add.save()
				form.save_m2m()
				alert = "suc"
				info = "La Categoria %s se guardo con exito" % (add.nombre)
			else:
				alert = "war"
				info = "esta madre esta mal"
			form = addCategoriaForm()
			ctx = {'form':form, 'informacion':info, 'alert':alert}
			return render_to_response('ventas/addcategoria.html',ctx, context_instance=RequestContext(request))
		else:
			form = addCategoriaForm()
			ctx = {'form':form}
			return render_to_response('ventas/addcategoria.html',ctx, context_instance=RequestContext(request))
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
	lista_productos = producto.objects.filter(status=True).filter(tienda=tienda_actual)
	paginator = Paginator(lista_productos, 5)

	pagina = request.GET.get('pagina')
	buscar = request.GET.get("buscar", "")
	try:
		prod = paginator.page(pagina)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		prod = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		prod = paginator.page(paginator.num_pages)

	return render(request,'ventas/productos.html',{'productos':prod, 'buscar':buscar})

def categorias_view(request):
	tienda_actual = request.user.get_profile().tienda
	categorias = categoria.objects.filter(tienda=tienda_actual)
	return render(request,'ventas/categorias.html',{'categorias':categorias})

def configuracion_tienda_view(request):
	return render(request,'ventas/configtienda.html')

def herramienta_view(request):
	return render(request,'ventas/herramientadiseno.html')

def confEnvios_view(request):
	return render(request,'ventas/conf-envios.html')

def producto_view(request,id_producto):
	prod = producto.objects.get(id=id_producto)
	return render(request,'ventas/producto.html',{'producto':prod})



def add(request):
	cart = Cart(request.session)
	product = producto.objects.get(id=request.GET.get('product_id'))
	cart.add(product, price=product.precio)
	return HttpResponse("Added")

def show(request):
	return render(request, 'ventas/show-cart.html')

def addCart(request):
	if request.method == "POST":
		formulario = addCartForm(request.POST)
		if formulario.is_valid():
			id_producto = formulario.cleaned_data['idproducto']
			cart = Cart(request.session)
			product = producto.objects.get(id=request.GET.get('product_id'))
			cart.add(product, price=product.precio)
			return HttpResponseRedirect()
	else:
		formulario = addCartForm()
	return HttpResponse("Added")