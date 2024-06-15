
from django.urls import path
# from . import views 
from .views import home, contacto, registro, agregar_al_carrito, ver_carrito

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',ver_carrito, name='ver_carrito'),
]