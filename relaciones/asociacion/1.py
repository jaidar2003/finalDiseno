class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = [] # aqui esta la asociacion

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def ensenar(self):
        print(f"{self.nombre} esta ensenando a: ")
        for estudiante in self.estudiantes:
            estudiante.estudiar()
            print(f"{estudiante.nombre}")

estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("Pedro")
profesor = Profesor("Maria")

profesor.agregar_estudiante(estudiante1)
profesor.agregar_estudiante(estudiante2)

profesor.ensenar()
#estudiante1.estudiar()
#estudiante2.estudiar()


# Asociacion linea recta >

# una propiedad de una clase contiene una referencia a una instancia de otra clase