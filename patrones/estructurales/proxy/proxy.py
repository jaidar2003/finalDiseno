from interfaz import Documento
from objeto_real import DocumentoConfidencial

class ProxyDocumento(Documento):
    def __init__(self, contenido, usuario):
        self.usuario = usuario
        self.documento_real = DocumentoConfidencial(contenido)

    def mostrar(self):
        if self.usuario == "admin":
            self.documento_real.mostrar()
        else:
            print("[ACCESO DENEGADO] Solo los administradores pueden ver este documento.")
