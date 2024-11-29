from django.contrib import admin
from .models import Producto, Pedido

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")
    list_filter = ("categoria",)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("numero_pedido", "fecha")
    list_filter = ("numero_pedido", "fecha",)
    date_hierarchy = "fecha"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)