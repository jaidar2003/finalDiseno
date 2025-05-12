from creadores import LogisticaMaritima, LogisticaTerrestre

def main():
    tipo = input("Ingrese el tipo de logística (terrestre/maritima): ").strip().lower()

    if tipo == "terrestre":
        logistica = LogisticaTerrestre()
    elif tipo == "maritima":
        logistica = LogisticaMaritima()
    else:
        print("Tipo de logística no válido.")
        return

    logistica.planificar_entrega()

if __name__ == "__main__":
    main()