# Patrón observer

```mermaid
classDiagram
    class Subject {
        +attach(Observer)
        +detach(Observer)
        +notify()
    }

    class ConcreteSubject {
        -estado
    }

    class Observer {
        +update()
    }

    class ConcreteObserver {
        +update()
    }

    Subject <|-- ConcreteSubject
    Observer <|-- ConcreteObserver
    ConcreteSubject --> Observer
```

## Explicación
**Subject**: mantiene la lista de observadores y notifica cambios.

**Observer**: interfaz para actualizarse ante eventos.

**ConcreteSubject**: cambia de estado y notifica.

**ConcreteObserver**: reacciona a los cambios en el Subject.
