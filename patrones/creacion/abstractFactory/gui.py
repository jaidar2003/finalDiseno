# Este patrón crea diferentes familias de objetos. Su objetivo principal es soportar múltiples estándares que
# vienen definidos por las diferentes jerarquías de herencia de objetos.

from abc import ABC, abstractmethod

# ==== Abstract Products ==== interfaz para los productos

class AbstractProductA(ABC):  # Botón
    @abstractmethod
    def render(self) -> str:
        pass

class AbstractProductB(ABC):  # Checkbox
    @abstractmethod
    def toggle(self) -> str:
        pass


# ==== Concrete Products ==== define un producto que la correspondiente factory se encarga de crear

class ProductA1(AbstractProductA):  # Botón Windows
    def render(self) -> str:
        return "Renderizando botón estilo Windows"

class ProductB1(AbstractProductB):  # Checkbox Windows
    def toggle(self) -> str:
        return "Checkbox Windows activado"

class ProductA2(AbstractProductA):  # Botón Mac
    def render(self) -> str:
        return "Renderizando botón estilo Mac"

class ProductB2(AbstractProductB):  # Checkbox Mac
    def toggle(self) -> str:
        return "Checkbox Mac activado"


# ==== Abstract Factory ==== interfaz para las fábricas

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


# ==== Concrete Factories ==== implementan operaciones para la creacion de objetos concretos

class FactoryConcreto1(AbstractFactory):  # Windows
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()

class FactoryConcreto2(AbstractFactory):  # Mac
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()


# ==== Cliente ==== utiliza solamente las interfaces

class Client:
    def __init__(self, factory: AbstractFactory):
        self.boton = factory.create_product_a()
        self.checkbox = factory.create_product_b()

    def mostrar_gui(self):
        print(self.boton.render())
        print(self.checkbox.toggle())


# ==== Uso del patrón ====

if __name__ == "__main__":
    print("🎯 Interfaz para Windows:")
    cliente_windows = Client(FactoryConcreto1())
    cliente_windows.mostrar_gui()

    print("\n🎯 Interfaz para MacOS:")
    cliente_mac = Client(FactoryConcreto2())
    cliente_mac.mostrar_gui()