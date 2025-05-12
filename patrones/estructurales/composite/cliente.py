from componente import Archivo, Carpeta

def main():
    # Crear archivos
    a1 = Archivo("tarea.docx")
    a2 = Archivo("informe.pdf")
    a3 = Archivo("foto.png")

    # Crear carpetas
    carpeta_trabajo = Carpeta("Trabajo")
    carpeta_personal = Carpeta("Personal")
    carpeta_raiz = Carpeta("Mi PC")

    # Armar estructura
    carpeta_trabajo.agregar(a1)
    carpeta_trabajo.agregar(a2)

    carpeta_personal.agregar(a3)

    carpeta_raiz.agregar(carpeta_trabajo)
    carpeta_raiz.agregar(carpeta_personal)

    # Mostrar estructura completa
    carpeta_raiz.mostrar()

if __name__ == "__main__":
    main()
