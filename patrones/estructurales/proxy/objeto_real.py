from interfaz import Documento

class DocumentoConfidencial(Documento):
    def __init__(self, contenido):
        self.contenido = contenido

    def mostrar(self):
        print(f"[ACCESO AL DOCUMENTO] Contenido: {self.contenido}")
