```mermaid
classDiagram
    class DatabaseConnection {
        - static _instance: DatabaseConnection
        - static _lock: Lock
        - connection: sqlite3.Connection
        + __new__(db_path: str): DatabaseConnection
        + get_connection(): sqlite3.Connection
    }

    note right of DatabaseConnection::_instance
        Atributo estático que guarda la única instancia
    end

    note right of DatabaseConnection::__new__
        Sobrescribe la creación del objeto para asegurar
        que siempre devuelva la misma instancia
    end

    note right of DatabaseConnection::get_connection
        Proporciona acceso global a la conexión
    end
```
### Patrón Singleton
El patrón Singleton asegura que una clase tenga una única instancia y proporciona un punto de acceso global a ella. Este patrón es útil cuando se necesita exactamente un objeto para coordinar acciones en todo el sistema.

### clase Abstracta: implementa una olantilla que define el esqueleto del algoritmo y define metodos abstractos que deben ser implementados por las subclases.

## clase Concreta: implementa los metodos abstractos definidos en la clase abstracta.