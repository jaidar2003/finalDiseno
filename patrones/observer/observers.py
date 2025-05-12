class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, canal, video):
        print(f"🔔 {self.nombre} fue notificado: Nuevo video en {canal} → {video}")
