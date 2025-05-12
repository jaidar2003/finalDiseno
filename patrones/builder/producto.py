class Computadora:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.almacenamiento = None
        self.gpu = None

    def especificaciones(self):
        print("Configuración de la Computadora:")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"GPU: {self.gpu}")
