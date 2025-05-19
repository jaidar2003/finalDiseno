```maremaid
classDiagram
    class Creator {
        +factoryMethod(): Product
    }
    class ConcreteCreator {
        +factoryMethod(): ConcreteProduct
    }
    class Product
    class ConcreteProduct

    Creator <|-- ConcreteCreator
    Product <|-- ConcreteProduct
    ConcreteCreator --> ConcreteProduct
```
# Creator: declara el método fábrica factoryMethod.

# ConcreteCreator: implementa ese método para retornar un ConcreteProduct.

# Product: interfaz del objeto a crear.

# ConcreteProduct: implementación real que se retorna.