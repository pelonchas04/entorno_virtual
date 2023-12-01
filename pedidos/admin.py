from django.contrib import admin
from pedidos.models import Cliente, Proveedor, Articulo

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre_completo", "email")
    search_fields=["nombre_completo"]

class ProveedorAdmin(admin.ModelAdmin):
    list_display=["nombre_pro"]
    search_fields=["nombre_pro"]

class ArticuloAdmin(admin.ModelAdmin):
    list_display=("articulo", "precio_venta", "marca")
    search_fields=("articulo", "modelo")
    list_filter=("marca",)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Articulo, ArticuloAdmin)