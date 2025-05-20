import sqlite3
from threading import Lock

class DatabaseConnection:
    # 🧠 Atributo de clase para guardar la única instancia
    _instance = None

    # 🔒 Lock para evitar condiciones de carrera si hay múltiples hilos
    _lock = Lock()

    def __new__(cls, db_path='mi_base.db'):
        # Sección crítica protegida por lock
        with cls._lock:
            # ✅ Si no existe una instancia, la crea
            if cls._instance is None:
                print("📡 Creando nueva conexión a la base de datos...")
                cls._instance = super(DatabaseConnection, cls).__new__(cls)

                # Establece la conexión a la base de datos y la guarda en la instancia
                cls._instance.connection = sqlite3.connect(db_path)
            else:
                # 🔁 Si ya existe una instancia, la reutiliza
                print("🔁 Reutilizando conexión existente...")
        # 🔁 Devuelve siempre la misma instancia
        return cls._instance

    def get_connection(self):
        # Punto de acceso global a la conexión
        return self.connection


# 🧪 Uso del patrón Singleton
if __name__ == "__main__":
    # Se crea la primera instancia (y se abre la conexión)
    db1 = DatabaseConnection().get_connection()

    # Se intenta crear otra, pero se reutiliza la anterior
    db2 = DatabaseConnection().get_connection()

    # ✅ Verifica que ambas variables apuntan al mismo objeto
    print(db1 is db2)  # 👉 True, ambas son la misma conexión

    # Ejemplo: crear una tabla solo si no existe
    cursor = db1.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ejemplo (id INTEGER PRIMARY KEY, nombre TEXT)")
    db1.commit()
