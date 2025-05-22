from models.detalle import Detalle
from controllers.producto_controller import ProductoController

class DetalleController:
    def __init__(self, producto_controller):
        self.producto_controller = producto_controller

    def crear_detalle(self, producto, cantidad):
        self.producto_controller.descontar_stock(producto, cantidad)
        return Detalle(producto, cantidad)
