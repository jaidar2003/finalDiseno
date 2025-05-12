class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerRuido(self):
        print("Este animal hace ruido")

class Perro(Animal):
    def hacerRuido(self):
        print("Este perro hace miau")

animal = Animal("Perro")
animal.hacerRuido()

perro = Perro("Perro")
perro.hacerRuido()

# herencia: una subclase hereda todas las propiedades y metodos de la clase padre, la subclase puede contener informacion adicional

