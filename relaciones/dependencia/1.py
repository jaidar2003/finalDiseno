class Documento:
    def __init__(self, contenido=None):
        self.contenido = contenido

class Impresora:
    def imprimir(self, documento):
        if documento is None:
            raise ValueError("No se puede imprimir un documento nulo")
        else:
            print(f"Imprimiendo: {documento.contenido}")

doc = Documento("Annuntio vobis gaudium magnum: habemus Papam, Eminentissimum ac Reverendissimum Dominum, \n"
                "Dominum Robertum Franciscum Sanctæ Romanæ Ecclesiæ Cardinale Prevost, qui sibi nomen imposuit León XIV.")
impresora = Impresora()
impresora.imprimir(doc)

# Dependencia ------>

# una clase depende de otra para funcionar, pero no es parte de su estructura