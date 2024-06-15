
from django.urls import path
# from . import views 
from .views import home, contacto, registro, carrito

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('carrito/', carrito, name="carrito"),
]