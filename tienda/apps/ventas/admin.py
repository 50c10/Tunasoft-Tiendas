from django.contrib import admin
from tienda.apps.ventas.models import cliente, producto, tienda, propiedades


admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(tienda)
admin.site.register(propiedades)
