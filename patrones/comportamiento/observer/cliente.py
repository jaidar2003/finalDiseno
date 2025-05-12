from subject import CanalYouTube
from observers import Usuario

def main():
    canal = CanalYouTube("Juanma Code")

    user1 = Usuario("Sofía")
    user2 = Usuario("Marcos")
    user3 = Usuario("Lucía")

    # Suscribirse
    canal.agregar_suscriptor(user1)
    canal.agregar_suscriptor(user2)

    # Publicar video
    canal.subir_video("Patrones de Diseño en Python")

    # Agregar otro usuario
    canal.agregar_suscriptor(user3)
    canal.subir_video("Cómo usar Observer con ejemplos")

    # Eliminar uno
    canal.eliminar_suscriptor(user1)
    canal.subir_video("Curso completo de Flask")

if __name__ == "__main__":
    main()
