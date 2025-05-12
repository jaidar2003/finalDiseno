from fabricas import Fabrica, FabricaDeMadera, FabricaDeMetal

def mostrar_muebles(fabrica):
    silla = fabrica.crear_silla()
    mesa = fabrica.crear_mesa()
    silla.sentarse()
    mesa.usar()

def main():
    estilo = input("Estilo: ")

    if estilo == "madera":
        fabrica = FabricaDeMadera()
    elif estilo == "metal":
        fabrica = FabricaDeMetal()
    else:
        print("Estilo no válido")
        return

    mostrar_muebles(fabrica)

if __name__ == "__main__":
    main()
