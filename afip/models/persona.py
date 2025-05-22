from abc import ABC, abstractmethod
from controllers.persona_controller import PersonaController

class Persona(ABC):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

        self.controlador = PersonaController()

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def agregar_factura(self, factura):
        self.controlador.agregar_factura(factura)