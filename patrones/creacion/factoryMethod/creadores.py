from abc import ABC, abstractmethod
from producto import Transporte, Camion, Barco


class Logistica(ABC):
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        pass

    def planificar_entrega(self):
        transporte = self.crear_transporte()
        transporte.entregar()

class LogisticaTerrestre(Logistica):
    def crear_transporte(self) -> Transporte:
        return Camion()

class LogisticaMaritima(Logistica):
    def crear_transporte(self) -> Transporte:
        return Barco()