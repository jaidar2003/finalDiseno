from abc import ABC, abstractmethod
from producto import Computadora

class BuilderComputadora(ABC):
    def __init__(self):
        self.computadora = Computadora()

    @abstractmethod
    def agregar_cpu(self): pass

    @abstractmethod
    def agregar_ram(self): pass

    @abstractmethod
    def agregar_almacenamiento(self): pass

    @abstractmethod
    def agregar_gpu(self): pass

    def obtener_resultado(self):
        return self.computadora

class ComputadoraGamerBuilder(BuilderComputadora):
    def agregar_cpu(self):
        self.computadora.cpu = "Intel i9"

    def agregar_ram(self):
        self.computadora.ram = "32GB"

    def agregar_almacenamiento(self):
        self.computadora.almacenamiento = "1TB SSD"

    def agregar_gpu(self):
        self.computadora.gpu = "NVIDIA RTX 4090"

class ComputadoraOficinaBuilder(BuilderComputadora):
    def agregar_cpu(self):
        self.computadora.cpu = "Intel i5"

    def agregar_ram(self):
        self.computadora.ram = "8GB"

    def agregar_almacenamiento(self):
        self.computadora.almacenamiento = "512GB SSD"

    def agregar_gpu(self):
        self.computadora.gpu = "Integrada"
