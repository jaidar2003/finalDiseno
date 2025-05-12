class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializado = False
        return cls._instance

    def __init__(self):
        if self._inicializado:
            return
        self.mensajes = []
        self._inicializado = True

    def log(self, mensaje):
        self.mensajes.append(mensaje)
        print(f"[LOG] {mensaje}")

    def mostrar_log(self):
        print("Historial de logs")
        for m in self.mensajes:
            print(m)