```mermaid
classDiagram
    class AbstractFactory {
        +createProductA(): AbstractProductA
        +createProductB(): AbstractProductB
    }

    class ConcreteFactory {
        +createProductA(): ConcreteProductA
        +createProductB(): ConcreteProductB
    }

    class AbstractProductA
    class AbstractProductB
    class ConcreteProductA
    class ConcreteProductB
    class Client

    AbstractFactory <|-- ConcreteFactory
    AbstractProductA <|-- ConcreteProductA
    AbstractProductB <|-- ConcreteProductB
    Client --> AbstractFactory
    Client --> AbstractProductA
    Client --> AbstractProductB

```
```python
# AbstractFactory: declara los métodos de creación de productos.
# ConcreteFactory: implementa esos métodos para retornar productos concretos.
# AbstractProductA: interfaz del primer tipo de producto.
# AbstractProductB: interfaz del segundo tipo de producto.
# ConcreteProductA: implementación real del primer tipo de producto.
# ConcreteProductB: implementación real del segundo tipo de producto.
```