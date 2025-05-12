from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class EncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.encender()

class ApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.apagar()

class EncenderVentilador(Comando):
    def __init__(self, ventilador):
        self.ventilador = ventilador

    def ejecutar(self):
        self.ventilador.encender()

class ApagarVentilador(Comando):
    def __init__(self, ventilador):
        self.ventilador = ventilador

    def ejecutar(self):
        self.ventilador.apagar()
