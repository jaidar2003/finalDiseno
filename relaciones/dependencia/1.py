class Documento:
    def __init__(self, contenido):
        self.contenido = contenido

class Impresora:
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento.contenido}")

doc = Documento("Annuntio Vobis Gaudium Magnum Habemus Papam")
impresora = Impresora()
impresora.imprimir(doc)