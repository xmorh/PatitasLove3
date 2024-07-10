from django.contrib import admin
from .models import Producto, Carrito, CarritoItem
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'marca', 'imagen')
    list_editable = ('nombre', 'precio')
    search_fields=('nombre')
    list_filter = ('marca')

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoItem)