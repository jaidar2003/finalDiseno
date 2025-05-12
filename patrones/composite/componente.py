from abc import ABC, abstractmethod

# Componente base
class ComponenteArchivo(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass


# Hoja (Leaf): archivo individual
class Archivo(ComponenteArchivo):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Archivo: {self.nombre}")


# Compuesto (Composite): carpeta que contiene archivos o más carpetas
class Carpeta(ComponenteArchivo):
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = []

    def agregar(self, componente: ComponenteArchivo):
        self.contenido.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"[Carpeta: {self.nombre}]")
        for elemento in self.contenido:
            elemento.mostrar(nivel + 1)
