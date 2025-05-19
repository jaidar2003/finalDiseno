```mermaid
classDiagram
    class Director {
        +construct(): Product
    }
    class Builder {
        +buildPartA()
        +buildPartB()
        +getResult(): Product
    }
    class ConcreteBuilder {
        +buildPartA()
        +buildPartB()
        +getResult(): Product
    }
    class Product

    Director --> Builder
    Builder <|-- ConcreteBuilder
    ConcreteBuilder --> Product
```

## Explicación
**Director**: construye un objeto usando el builder.

**Builder**: define los pasos de construcción.

**ConcreteBuilder**: construye partes específicas del objeto.

**Product**: resultado final del proceso.