from django.shortcuts import render
# from .models import Producto

# Create your views here.

def home(request):
    # productos = Producto.objects.all()
    # data = {
    #     'productos': productos
    # }
    # se saco esto en el return , data
    return render(request, 'patitasLove/home.html')

def contacto(request):
    return render(request, 'patitasLove/contacto.html')

def registro(request):
    return render(request, 'patitasLove/registro.html')

def sesion(request):
    return render(request, 'patitasLove/sesion.html')

def carrito(request):
    return render(request, 'patitasLove/carrito.html')