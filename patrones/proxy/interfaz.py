from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def mostrar(self):
        pass
