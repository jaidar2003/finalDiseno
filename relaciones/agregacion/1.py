class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = [] # Agregacion

    def agregarAlumno(self, alumno):
        self.alumnos.append(alumno)

    def listarAlumnos(self):
        print(f"Los alumnos de {self.nombre} son: ")
        for alumno in self.alumnos:
            print(f"{alumno.nombre}")

juanma = Alumno("Juanma")
pedro = Alumno("Pedro")

curso = Curso("Python")
curso.agregarAlumno(juanma)
curso.agregarAlumno(pedro)

curso.listarAlumnos()