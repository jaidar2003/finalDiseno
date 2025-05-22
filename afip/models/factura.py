class Factura:
    def __init__(self, fecha, tipo, cliente, administrativo):
        self.fecha = fecha
        self.tipo = tipo
        self.cliente = cliente
        self.administrativo = administrativo
        self.detalles = []
        self.controlador = None

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)