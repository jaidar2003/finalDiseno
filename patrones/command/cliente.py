from dispositivos import Luz, Ventilador
from comandos import EncenderLuz, ApagarLuz, EncenderVentilador, ApagarVentilador
from control import ControlRemoto

def main():
    luz = Luz()
    ventilador = Ventilador()
    control = ControlRemoto()

    control.set_comando(EncenderLuz(luz))
    control.presionar_boton()

    control.set_comando(ApagarLuz(luz))
    control.presionar_boton()

    control.set_comando(EncenderVentilador(ventilador))
    control.presionar_boton()

    control.set_comando(ApagarVentilador(ventilador))
    control.presionar_boton()

if __name__ == "__main__":
    main()
