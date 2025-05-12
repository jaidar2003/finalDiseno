from estados import EstadoDetenido

class ReproductorMusica:
    def __init__(self):
        self.estado = EstadoDetenido()

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def reproducir(self):
        self.estado.reproducir(self)

    def pausar(self):
        self.estado.pausar(self)

    def detener(self):
        self.estado.detener(self)
