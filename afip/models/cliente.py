from models.persona import Persona

class Cliente(Persona):
    """
    Clase que representa a un cliente en el sistema.

    Hereda de la clase abstracta Persona e implementa atributos específicos
    para los clientes, como el tipo de responsabilidad fiscal.

    Atributos:
        nombre (str): Heredado de Persona, nombre del cliente
        apellido (str): Heredado de Persona, apellido del cliente
        tipo_responsable (str): Tipo de responsabilidad fiscal del cliente
                               (ej: "Responsable Inscripto", "Consumidor Final")
        controlador (PersonaController): Heredado de Persona, maneja las facturas del cliente
    """
    def __init__(self, nombre, apellido, tipo_responsable):
        """
        Constructor de la clase Cliente.

        Args:
            nombre (str): Nombre del cliente
            apellido (str): Apellido del cliente
            tipo_responsable (str): Tipo de responsabilidad fiscal del cliente
        """
        # Llamada al constructor de la clase padre
        super().__init__(nombre, apellido)
        self.tipo_responsable = tipo_responsable
