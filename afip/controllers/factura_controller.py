from models.factura import Factura

class FacturaController:
    def __init__(self, detalle_controller):
        self.detalle_controller = detalle_controller

    def crear_factura(self, fecha, tipo, cliente, administrativo):
        factura = Factura(fecha, tipo, cliente, administrativo)
        factura.controlador = self  # Set the controller on the factura instance
        cliente.agregar_factura(factura)
        administrativo.agregar_factura(factura)
        return factura

    def agregar_detalle(self, factura, producto, cantidad):
        detalle = self.detalle_controller.crear_detalle(producto, cantidad)
        factura.agregar_detalle(detalle)
        return factura

    def total(self, factura):
        return sum(d.subtotal for d in factura.detalles)