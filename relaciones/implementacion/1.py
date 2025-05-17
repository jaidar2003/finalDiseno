from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 4 * self.ancho

figura = Cuadrado(10, 10)
print('Area:', figura.area())
print('Perimetro:', figura.perimetro())

# Implementacion ------|>

# una clase implementa una interfaz y los metodos de la clase implementan todos los metodos declarados por la interfaz