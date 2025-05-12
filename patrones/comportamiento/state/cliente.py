from reproductor import ReproductorMusica

def main():
    r = ReproductorMusica()

    r.reproducir()  # Comienza a reproducir
    r.pausar()      # Pausa
    r.reproducir()  # Reanuda
    r.detener()     # Detiene
    r.pausar()      # No se puede
    r.detener()     # Ya estaba detenido

if __name__ == "__main__":
    main()
