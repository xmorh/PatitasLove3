from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio}"
    
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto, through='CarritoItem')

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"