
from django.urls import path
# from . import views 
from .views import home, contacto, registro, agregar_al_carrito, ver_carrito, agregar_producto, listar_producto, editar_producto, eliminar_producto, crear_venta, pago_exitoso, listar_ventas, descargar_ventas_excel

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',ver_carrito, name='ver_carrito'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('listar_producto/', listar_producto, name='listar_producto'),
    path('editar_producto/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('crear_venta/', crear_venta, name='crear_venta'),    
    path('pago_exitoso/', pago_exitoso, name='pago_exitoso'),
    path('listar_ventas/', listar_ventas, name='listar_ventas'),
    path('descargar_ventas_excel/', descargar_ventas_excel, name='descargar_ventas_excel'),
]