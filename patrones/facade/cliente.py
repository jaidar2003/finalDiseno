from fachada import CineFacade

def main():
    cine = CineFacade()
    cine.comprar_entrada("Matrix Resurrections", 12, 1500)

if __name__ == "__main__":
    main()
