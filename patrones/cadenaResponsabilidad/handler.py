from abc import ABC, abstractmethod

class ManejadorSoporte(ABC):
    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    @abstractmethod
    def manejar(self, problema):
        pass


class SoporteBasico(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "contraseña":
            print("Soporte Básico: Resolviendo problema de contraseña.")
        elif self.siguiente:
            self.siguiente.manejar(problema)
        else:
            print("Soporte Básico: No puedo manejar este problema.")


class SoporteIntermedio(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "software":
            print("Soporte Intermedio: Resolviendo problema de software.")
        elif self.siguiente:
            self.siguiente.manejar(problema)
        else:
            print("Soporte Intermedio: No puedo manejar este problema.")


class SoporteAvanzado(ManejadorSoporte):
    def manejar(self, problema):
        if problema == "hardware":
            print("Soporte Avanzado: Resolviendo problema de hardware.")
        elif self.siguiente:
            self.siguiente.manejar(problema)
        else:
            print("Soporte Avanzado: No puedo manejar este problema.")
