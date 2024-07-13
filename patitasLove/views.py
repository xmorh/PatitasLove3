import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoItem, Venta, VentaProducto
from .forms import ProductoForm
from django.core import serializers
from django.db.models import Q
from datetime import datetime
import re

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
        'total': total,
    }
    return render(request, 'patitasLove/carrito.html', data)

# def eliminar_del_carrito(request, producto_id):
#     carrito_id = request.session.get('carrito_id')
#     carrito = get_object_or_404(Carrito, id=carrito_id)
#     producto = get_object_or_404(Producto, id=producto_id)
#     item = CarritoItem.objects.get(carrito=carrito, producto=producto)
#     item.delete()

#     return redirect('ver_carrito')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario

    return render(request, 'patitasLove/producto/agregar.html', data)

def listar_producto(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos
    }
    return render(request, 'patitasLove/producto/listar.html', data)

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            # data["mensaje"] = "Editado Correctamente"
            return redirect(to='listar_producto')
        data["form"] = formulario
    return render(request,'patitasLove/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar_producto')

# def crear_venta(request):
#     venta = Venta.objects.create()
#     carrito_id = request.session.get('carrito_id')
#     if request.method == 'POST':
#         data = CarritoItem.objects.all()
#         carrito_items_json = serializers.serialize('json', data)
#         carrito_items = json.loads(carrito_items_json)  # Convertir cadena JSON a lista de diccionarios
        
#         carrito_items_filtrados = [item for item in carrito_items if item['fields']['carrito'] == carrito_id]

#         for carrito_item in carrito_items_filtrados:
#             producto = Producto.objects.get(id=carrito_item['fields']['producto'])
#             item, created = VentaProducto.objects.get_or_create(venta=venta, producto=producto)
            
#             if carrito_item['fields']['cantidad'] > 1:
#                 item.cantidad = carrito_item['fields']['cantidad']
#                 item.save()

#     return redirect(to='pago_exitoso')

def crear_venta(request):
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        # Si no hay carrito, redirigir a la página de carrito
        return redirect('ver_carrito')

    carrito = get_object_or_404(Carrito, id=carrito_id)
    items = CarritoItem.objects.filter(carrito=carrito)

    if not items.exists():
        # Si no hay ítems en el carrito, redirigir a la página de carrito
        return redirect('ver_carrito')

    venta = Venta.objects.create()

    for item in items:
        VentaProducto.objects.create(venta=venta, producto=item.producto, cantidad=item.cantidad)
    
    # Eliminar todos los ítems del carrito
    items.delete()

    # Limpiar el carrito de la sesión
    del request.session['carrito_id']

    return redirect('pago_exitoso')

def pago_exitoso(request):
    return render(request, 'patitasLove/pago_exitoso.html')

def listar_ventas(request):
    # Obtener las ventas
    ventas = Venta.objects.all()

    # Obtener los parámetros de fecha desde y hasta de la solicitud GET
    fecha_desde_str = request.GET.get('fecha_desde')
    fecha_hasta_str = request.GET.get('fecha_hasta')

    # Convertir las cadenas de fecha a objetos datetime si existen
    if fecha_desde_str and fecha_hasta_str:
        fecha_desde = datetime.strptime(fecha_desde_str, '%Y-%m-%d').date()
        fecha_hasta = datetime.strptime(fecha_hasta_str, '%Y-%m-%d').date()

        # Filtrar las ventas por fecha usando Q objects para combinar condiciones OR
        ventas = ventas.filter(
            Q(fecha__date__gte=fecha_desde) &
            Q(fecha__date__lte=fecha_hasta)
        )

    # Contexto para pasar a la plantilla
    data = {
        'ventas': ventas
    }

    return render(request, 'patitasLove/ventas/listar_ventas.html', data)
