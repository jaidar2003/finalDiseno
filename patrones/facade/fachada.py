from subsistemas import Pantalla, SistemaDeAsientos, SistemaDePago

class CineFacade:
    def __init__(self):
        self.pantalla = Pantalla()
        self.asientos = SistemaDeAsientos()
        self.pago = SistemaDePago()

    def comprar_entrada(self, pelicula, asiento, monto):
        print("Iniciando compra de entrada...")
        self.pantalla.mostrar_pelicula(pelicula)
        self.asientos.reservar_asiento(asiento)
        self.pago.procesar_pago(monto)
        print("¡Compra completada!")
