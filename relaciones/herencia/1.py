class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerRuido(self):
        print("Este animal hace ruido")

class Perro(Animal):
    def hacerRuido(self):
        print("Este perro hace miau")

    def comer(self):
        print("Este perro come croquetas")

animal = Animal("Perro")
animal.hacerRuido()
# animal.comer() # no se puede llamar a la funcion comer porque no existe en la clase Animal

perro = Perro("Perro")
perro.hacerRuido()
perro.comer()

# Herencia linea recta |>

# una subclase hereda todas las funciones de la clase principal, las subclases pueden contener informacion adicional