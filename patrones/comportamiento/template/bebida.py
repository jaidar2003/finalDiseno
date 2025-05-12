from abc import ABC, abstractmethod

class Bebida(ABC):
    def preparar(self):
        self.hervir_agua()
        self.agregar_principal()
        self.servir()

    def hervir_agua(self):
        print("🔥 Hirviendo agua...")

    @abstractmethod
    def agregar_principal(self):
        pass

    def servir(self):
        print("🥤 Sirviendo en vaso.")

class Te(Bebida):
    def agregar_principal(self):
        print("🍵 Agregando saquito de té.")

class Cafe(Bebida):
    def agregar_principal(self):
        print("☕ Agregando café molido.")
