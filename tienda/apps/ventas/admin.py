from django.contrib import admin
from tienda.apps.ventas.models import cliente, producto, tienda, propiedades, categoria, imagen


admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(tienda)
admin.site.register(propiedades)
admin.site.register(categoria)
admin.site.register(imagen)
