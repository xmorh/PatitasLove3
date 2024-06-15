from django.shortcuts import render, redirect
from .models import Producto
from .carrito import Carrito

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }

    return render(request, 'patitasLove/home.html', data)

def contacto(request):
    return render(request, 'patitasLove/contacto.html')

def registro(request):
    return render(request, 'patitasLove/registro.html')

def sesion(request):
    return render(request, 'patitasLove/sesion.html')

def carrito(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'patitasLove/carrito.html', data)

def agregarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Carrito")

def eliminarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Carro")

def restarP(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Carro")    

def limpiarP(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Carro")    
    
def total_carrito(request):
    carrito = Carrito(request)
    return render(request, 'patitasLove/carrito.html', {'carrito': carrito})