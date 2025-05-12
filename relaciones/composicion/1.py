class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def arrancar(self):
        print(f"El motor {self.tipo} ha arrancado")


class Auto:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = Motor(motor)  # Composición: el Auto crea y posee su Motor

    def encender(self):
        print(f"El auto {self.marca} ha sido encendido")
        self.motor.arrancar()


auto = Auto("Toyota", "V6")
auto.encender()  # <- esto sí llama al método
