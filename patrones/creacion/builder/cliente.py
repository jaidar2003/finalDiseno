from builder import ComputadoraGamerBuilder, ComputadoraOficinaBuilder

def construir(builder):
    builder.agregar_cpu()
    builder.agregar_ram()
    builder.agregar_almacenamiento()
    builder.agregar_gpu()
    return builder.obtener_resultado()

def main():
    tipo = input("¿Qué tipo de PC querés? (gamer/oficina): ").strip().lower()

    if tipo == "gamer":
        builder = ComputadoraGamerBuilder()
    elif tipo == "oficina":
        builder = ComputadoraOficinaBuilder()
    else:
        print("Tipo no válido.")
        return

    pc = construir(builder)
    pc.especificaciones()

if __name__ == "__main__":
    main()
