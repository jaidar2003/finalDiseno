from models.cliente import Cliente
from models.administrativo import Administrativo

class PersonaController:
    def __init__(self):
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def mostrar_facturas(self, nombre_completo):
        if not self.facturas:
            print(f"{nombre_completo} no tiene facturas.")
            return

        print(f"Facturas de {nombre_completo}:")
        for i, factura in enumerate(self.facturas, 1):
            print(f"{i}. {factura}")

    def crear_cliente(self, nombre, apellido, tipo_responsable):
        return Cliente(nombre, apellido, tipo_responsable)

    def crear_administrativo(self, nombre, apellido, cargo):
        return Administrativo(nombre, apellido, cargo)

    def get_facturas(self, persona):
        return persona.controlador.facturas
