class ControlRemoto:
    def __init__(self):
        self._comando = None

    def set_comando(self, comando):
        self._comando = comando

    def presionar_boton(self):
        if self._comando:
            self._comando.ejecutar()
        else:
            print("⚠️ No hay comando asignado")
