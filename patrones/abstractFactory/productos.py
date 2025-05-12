from abc import ABC, abstractmethod

# PRODUCTO A

class Silla(ABC):
    @abstractmethod
    def sentarse(self):
        pass

class SillaDeMadera(Silla):
    def sentarse(self):
        print("Sentarse en una silla de madera")

class SillaDeMetal(Silla):
    def sentarse(self):
        print("Sentarse en una silla de metal")


# PRODUCTO B

class Mesa(ABC):
    @abstractmethod
    def usar(self):
        pass

class MesaDeMadera(Mesa):
    def usar(self):
        print("Usar una mesa de madera")

class MesaDeMetal(Mesa):
    def usar(self):
        print("Usar una mesa de metal")
