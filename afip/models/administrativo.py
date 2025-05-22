from models.persona import Persona

class Administrativo(Persona):
    """
    Clase que representa a un administrativo o empleado en el sistema.

    Hereda de la clase abstracta Persona e implementa atributos específicos
    para los administrativos, como el cargo que ocupan en la organización.

    Atributos:
        nombre (str): Heredado de Persona, nombre del administrativo
        apellido (str): Heredado de Persona, apellido del administrativo
        cargo (str): Cargo o posición que ocupa el administrativo en la organización
        controlador (PersonaController): Heredado de Persona, maneja las facturas del administrativo
    """
    def __init__(self, nombre, apellido, cargo):
        """
        Constructor de la clase Administrativo.

        Args:
            nombre (str): Nombre del administrativo
            apellido (str): Apellido del administrativo
            cargo (str): Cargo o posición en la organización
        """
        # Llamada al constructor de la clase padre
        super().__init__(nombre, apellido)
        self.cargo = cargo
