from abc import ABC, abstractmethod
from productos import Silla, SillaDeMadera, SillaDeMetal, Mesa, MesaDeMadera, MesaDeMetal

class Fabrica(ABC):
    @abstractmethod
    def crear_silla(self) -> Silla:
        pass

    @abstractmethod
    def crear_mesa(self) -> Mesa:
        pass

class FabricaDeMadera(Fabrica):
    def crear_silla(self) -> Silla:
        return SillaDeMadera()

    def crear_mesa(self) -> Mesa:
        return MesaDeMadera()

class FabricaDeMetal(Fabrica):
    def crear_silla(self) -> Silla:
        return SillaDeMetal()

    def crear_mesa(self) -> Mesa:
        return MesaDeMetal()