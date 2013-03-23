from django.contrib import admin
from tienda.apps.ventas.models import cliente, producto


admin.site.register(cliente)
admin.site.register(producto)