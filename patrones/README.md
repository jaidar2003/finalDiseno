%%{init: {'theme': 'default'}}%%
classDiagram
class "Patrón" {
  +Nombre
  +Tipo
  +Problema que resuelve
  +Ejemplo armado
}

class FactoryMethod {
  +Creacional
  +Delegar la creación de objetos a subclases
  +Crear transporte (camión/barco)
}
class AbstractFactory {
  +Creacional
  +Crear familias de objetos relacionados
  +Muebles modernos/victorianos
}
class Singleton {
  +Creacional
  +Garantizar única instancia global
  +Logger único
}
class Builder {
  +Creacional
  +Construir objeto complejo paso a paso
  +PC Gamer u Oficina
}
class Composite {
  +Estructural
  +Tratar objetos individuales y compuestos igual
  +Sistema de archivos (carpetas y archivos)
}
class Facade {
  +Estructural
  +Simplificar interfaz a subsistemas complejos
  +Sistema de cine
}
class Proxy {
  +Estructural
  +Controlar acceso a objeto real
  +Documento confidencial
}
class ChainOfResponsibility {
  +Comportamiento
  +Pasar petición por una cadena de handlers
  +Soporte técnico (básico → avanzado)
}
class Command {
  +Comportamiento
  +Encapsular acción como objeto
  +Control remoto
}
class Observer {
  +Comportamiento
  +Notificar automáticamente a suscriptores
  +Canal de YouTube y usuarios
}
class State {
  +Comportamiento
  +Cambiar comportamiento según estado
  +Reproductor de música

}

Patrón <|-- FactoryMethod
Patrón <|-- AbstractFactory
Patrón <|-- Singleton
Patrón <|-- Builder
Patrón <|-- Composite
Patrón <|-- Facade
Patrón <|-- Proxy
Patrón <|-- ChainOfResponsibility
Patrón <|-- Command
Patrón <|-- Observer
Patrón <|-- State
