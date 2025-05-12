from bebida import Te, Cafe

def main():
    print("Preparando té:")
    te = Te()
    te.preparar()

    print("\nPreparando café:")
    cafe = Cafe()
    cafe.preparar()

if __name__ == "__main__":
    main()
