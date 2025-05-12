from handler import SoporteBasico, SoporteIntermedio, SoporteAvanzado

def main():
    # Crear los manejadores
    basico = SoporteBasico()
    intermedio = SoporteIntermedio()
    avanzado = SoporteAvanzado()

    # Armar la cadena: básico → intermedio → avanzado
    basico.set_siguiente(intermedio)
    intermedio.set_siguiente(avanzado)

    # Simular problemas
    problemas = ["contraseña", "software", "hardware", "impresora"]

    for p in problemas:
        print(f"\nSolicitud: problema de {p}")
        basico.manejar(p)

if __name__ == "__main__":
    main()
