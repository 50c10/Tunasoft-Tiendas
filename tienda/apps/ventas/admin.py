from django.contrib import admin
from tienda.apps.ventas.models import cliente, producto, tienda


admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(tienda)
