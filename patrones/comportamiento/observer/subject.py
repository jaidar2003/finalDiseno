class CanalYouTube:
    def __init__(self, nombre):
        self.nombre = nombre
        self._suscriptores = []

    def agregar_suscriptor(self, observador):
        self._suscriptores.append(observador)

    def eliminar_suscriptor(self, observador):
        self._suscriptores.remove(observador)

    def notificar(self, video):
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(self.nombre, video)

    def subir_video(self, titulo):
        print(f"📹 {self.nombre} subió un nuevo video: {titulo}")
        self.notificar(titulo)
