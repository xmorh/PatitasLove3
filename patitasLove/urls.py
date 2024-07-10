
from django.urls import path
# from . import views 
from .views import home, contacto, registro, agregar_al_carrito, ver_carrito, agregar_producto, listar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',ver_carrito, name='ver_carrito'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('listar_producto/', listar_producto, name='listar_producto'),
]