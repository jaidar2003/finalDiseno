from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def reproducir(self, reproductor): pass

    @abstractmethod
    def pausar(self, reproductor): pass

    @abstractmethod
    def detener(self, reproductor): pass


class EstadoReproduciendo(Estado):
    def reproducir(self, r): print("🔁 Ya está reproduciendo.")
    def pausar(self, r):
        print("⏸ Pausando...")
        r.set_estado(EstadoPausado())

    def detener(self, r):
        print("⏹ Deteniendo...")
        r.set_estado(EstadoDetenido())


class EstadoPausado(Estado):
    def reproducir(self, r):
        print("▶️ Reanudando reproducción...")
        r.set_estado(EstadoReproduciendo())

    def pausar(self, r): print("⏸ Ya está pausado.")
    def detener(self, r):
        print("⏹ Deteniendo desde pausa...")
        r.set_estado(EstadoDetenido())


class EstadoDetenido(Estado):
    def reproducir(self, r):
        print("▶️ Comenzando a reproducir...")
        r.set_estado(EstadoReproduciendo())

    def pausar(self, r): print("⚠️ No se puede pausar: está detenido.")
    def detener(self, r): print("⏹ Ya está detenido.")
