# sirve para construir algoritmos u objetos complejos a partir de otros más simples y similares entre sí
from abc import ABC, abstractmethod

# ==== Component ==== implementa un comportamiento común entre las clases y declara una interfaz de manipulacion
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    def add(self, component: 'Component'):
        pass

    def remove(self, component: 'Component'):
        pass

    def get_child(self, index: int) -> 'Component':
        return None


# ==== Leaf ==== define comportamientos de los objetos primitivos
class Archivo(Component):
    def __init__(self, nombre):
        self.nombre = nombre

    def operation(self) -> str:
        return f"📄 Archivo: {self.nombre}"


# ==== Composite ==== define comportamientos de los objetos compuestos (objetos con hijos)
class Carpeta(Component):
    def __init__(self, nombre):
        self.nombre = nombre
        self._hijos = []

    def add(self, component: Component):
        self._hijos.append(component)

    def remove(self, component: Component):
        self._hijos.remove(component)

    def get_child(self, index: int) -> Component:
        return self._hijos[index]

    def operation(self) -> str:
        resultado = [f"📁 Carpeta: {self.nombre}"]
        for hijo in self._hijos:
            resultado.append(f"  {hijo.operation()}")
        return '\n'.join(resultado)


# ==== Cliente ==== manipula objetos de la composicion a traves de component
def mostrar_estructura(component: Component):
    print(component.operation())


# ==== Uso del patrón ====
if __name__ == "__main__":
    # Crear archivos
    archivo1 = Archivo("cv.pdf")
    archivo2 = Archivo("foto.png")
    archivo3 = Archivo("informe.docx")

    # Crear carpetas
    carpeta1 = Carpeta("Documentos")
    carpeta2 = Carpeta("Imágenes")
    carpeta_principal = Carpeta("Mi PC")

    # Armar estructura
    carpeta1.add(archivo1)
    carpeta2.add(archivo2)
    carpeta1.add(archivo3)

    carpeta_principal.add(carpeta1)
    carpeta_principal.add(carpeta2)

    # Mostrar
    mostrar_estructura(carpeta_principal)