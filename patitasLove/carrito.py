class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregarP(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += producto.precio
        self.guardarP()

    def guardarP(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminarP(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardarP()
    
    def restarP(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["precio"] -= producto.precio
                if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
                self.guardarP()
    
    def limpiarP(self):
        self.session["carrito"] = {}
        self.session.modified = True