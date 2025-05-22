class ProductoController:
    def crear_producto(self, nombre, precio, stock):
        from models.producto import Producto
        return Producto(nombre, precio, stock)

    def descontar_stock(self, producto, cantidad):
        if cantidad > producto.stock:
            raise ValueError(f"No hay suficiente stock de {producto.nombre}")
        producto.stock -= cantidad
        return producto
