# Define una estructura algorítmica cuya lógica quedará a cargo de las subclases.
from abc import ABC, abstractmethod

# Clase abstracta (Template)
# Se implementa un metodo plantilla que define el esqueleto del algoritmo, y define metodos abstractos que deben de ser implementados por sub clases

class BebidaCaliente(ABC):
    def preparar(self):
        self.hervir_agua()
        self.agregar_ingrediente_principal()
        self.servir_en_taza()
        self.agregar_condimentos()

    def hervir_agua(self):
        print("Hirviendo agua...")

    def servir_en_taza(self):
        print("Sirviendo en la taza...")

    @abstractmethod
    def agregar_ingrediente_principal(self):
        pass

    @abstractmethod
    def agregar_condimentos(self):
        pass


# Subclase concreta: Té
# Implementa los metodos abstractos de la clase base para realizar su propia logica
class Te(BebidaCaliente):
    def agregar_ingrediente_principal(self):
        print("Agregando la bolsita de té...")

    def agregar_condimentos(self):
        print("Agregando limón...")

# Subclase concreta: Café
class Cafe(BebidaCaliente):
    def agregar_ingrediente_principal(self):
        print("Agregando café instantáneo...")

    def agregar_condimentos(self):
        print("Agregando azúcar y leche...")

# Uso del patrón
def preparar_bebida(bebida: BebidaCaliente):
    bebida.preparar()

# Ejecutar ejemplo
if __name__ == "__main__":
    print("☕ Preparando café:")
    preparar_bebida(Cafe())

    print("\n🍵 Preparando té:")
    preparar_bebida(Te())









# BebidaCaliente define el método plantilla preparar(), que establece el orden de los pasos.

# Métodos como hervir_agua y servir_en_taza son comunes y no varían.

#Métodos como agregar_ingrediente_principal y agregar_condimentos son abstractos: cada subclase los implementa a su manera.