# Patrón state

```mermaid
classDiagram
    class Context {
        -state: State
        +setState(State)
        +request()
    }

    class State {
        +handle(Context)
    }

    class EstadoA {
        +handle(Context)
    }

    class EstadoB {
        +handle(Context)
    }

    State <|-- EstadoA
    State <|-- EstadoB
    Context --> State
```

## Explicación
**Context**: mantiene una referencia a un objeto de estado actual.

**State**: define la interfaz común para estados.

**EstadoA / EstadoB**: implementan comportamientos específicos y pueden cambiar el estado del contexto.
