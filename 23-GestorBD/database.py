import sqlite3
from contextlib import closing
from pathlib import Path


class UserRepository:
    def __init__(self, ruta_bd):
        self.ruta_bd = Path(ruta_bd)

    def _conectar(self):
        return sqlite3.connect(self.ruta_bd)

    def crear_bd(self):
        # parents=True crea carpetas anidadas; exist_ok=True no falla si ya existe
        self.ruta_bd.parent.mkdir(parents=True, exist_ok=True)
        with closing(self._conectar()) as con:
            with con:  # commit automático (o rollback si hay error)
                con.execute("""
                    CREATE TABLE IF NOT EXISTS USER (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre VARCHAR(50) NOT NULL,
                        apellido VARCHAR(50) NOT NULL,
                        password VARCHAR(50) NOT NULL,
                        addres VARCHAR(50) NOT NULL
                    )
                """)

    def insertar(self, nombre, apellido, password, address):
        with closing(self._conectar()) as con:
            with con:
                con.execute(
                    "INSERT INTO USER (nombre, apellido, password, addres) "
                    "VALUES (?, ?, ?, ?)",
                    (nombre, apellido, password, address),
                )

    def actualizar(self, nombre, apellido, password, address, id_usuario):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(
                    "UPDATE USER SET nombre=?, apellido=?, password=?, addres=? "
                    "WHERE id=?",
                    (nombre, apellido, password, address, id_usuario),
                )
                return cursor.rowcount > 0

    def buscar_por_id(self, id_usuario):
        with closing(self._conectar()) as con:
            cursor = con.execute("SELECT * FROM USER WHERE id=?", (id_usuario,))
            return cursor.fetchone()#Devuelve como Tupla

    def eliminar(self, id_usuario):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute("DELETE FROM USER WHERE id=?", (id_usuario,))
                return cursor.rowcount > 0
