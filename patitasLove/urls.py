from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
# from . import views 
from .views import home, contacto, registro,sesion, carrito
from .views import agregarP, eliminarP, restarP, limpiarP, total_carrito

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('sesion/', sesion, name="sesion"),
    path('carrito/', carrito, name="carrito"),
    path('agregar/<int:producto_id>/', agregarP, name="agregar"),
    path('eliminar/<int:producto_id>/', eliminarP, name="eliminar"),
    path('restar/<int:producto_id>/', restarP, name="restar"),
    path('limpiar/', limpiarP, name="limpiar"),
]