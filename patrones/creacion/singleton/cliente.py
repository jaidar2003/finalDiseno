from logger import Logger

def main():
    logger1 = Logger()
    logger1.log("Primera entrada al sistema")

    logger2 = Logger()
    logger2.log("Segunda entrada al sistema")

    print("Logger 1 y Logger 2 son el mismo objeto?:", logger1 is logger2)

    logger1.mostrar_log()

if __name__ == "__main__":
    main()
