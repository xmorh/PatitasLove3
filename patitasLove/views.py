from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoItem

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    # se saco esto en el return , data
    return render(request, 'patitasLove/home.html', data)

def contacto(request):
    return render(request, 'patitasLove/contacto.html')

def registro(request):
    return render(request, 'patitasLove/registro.html')

def sesion(request):
    return render(request, 'patitasLove/sesion.html')

def agregar_al_carrito(request, producto_id):
   
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_id = request.session.get('carrito_id')

    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id

    item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        item.cantidad += 1
        item.save()

 
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        items = CarritoItem.objects.filter(carrito=carrito)
        total = sum(item.subtotal() for item in items)
    else:
        carrito = None
        items = []
        total = 0
    
    data = {
        'items': items,
        'total': total
    }
    return render(request, 'patitasLove/carrito.html', data)

# def eliminar_del_carrito(request, producto_id):
#     carrito_id = request.session.get('carrito_id')
#     carrito = get_object_or_404(Carrito, id=carrito_id)
#     producto = get_object_or_404(Producto, id=producto_id)
#     item = CarritoItem.objects.get(carrito=carrito, producto=producto)
#     item.delete()

#     return redirect('ver_carrito')