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

## Explicación
**AbstractFactory**: declara los métodos para crear productos abstractos.

**ConcreteFactory**: implementa los métodos para crear productos concretos.

**AbstractProductA / B**: interfaz para los productos.

**ConcreteProductA / B**: implementación real de productos.

**Client**: usa solo las interfaces sin conocer clases concretas.
