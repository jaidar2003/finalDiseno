# Patrón chainOfResponsibility

```mermaid
classDiagram
    class Handler {
        +setNext(Handler)
        +handleRequest()
    }

    class ConcreteHandler1 {
        +handleRequest()
    }

    class ConcreteHandler2 {
        +handleRequest()
    }

    Handler <|-- ConcreteHandler1
    Handler <|-- ConcreteHandler2
    ConcreteHandler1 --> Handler
```

## Explicación
**Handler**: interfaz base con método para manejar y establecer el siguiente manejador.

**ConcreteHandler**: maneja la solicitud o la pasa al siguiente.

**Cliente**: inicia la cadena sin conocer la estructura interna.
