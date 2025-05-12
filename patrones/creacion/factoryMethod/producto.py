from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass


class Camion(Transporte):
    def entregar(self):
        print("Entregar por camion")


class Barco(Transporte):
    def entregar(self):
        print("Entregar por barco")