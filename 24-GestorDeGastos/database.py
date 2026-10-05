import sqlite3
from contextlib import closing
from pathlib import Path

SQL_CREATEBD = """
                CREATE TABLE IF NOT EXISTS CATEGORIA (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE
                );

                CREATE TABLE IF NOT EXISTS GASTO (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descripcion TEXT NOT NULL,
                    monto REAL NOT NULL CHECK(monto > 0),
                    categoria_id INTEGER NOT NULL,
                    fecha TEXT NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES CATEGORIA(id) ON DELETE RESTRICT
                );
                """

SQL_INSERT_CAT = "INSERT INTO CATEGORIA(nombre) VALUES (?)"
SQL_UPDATE_CAT = "UPDATE CATEGORIA SET nombre=? WHERE id=?"
SQL_READ_CAT = "SELECT * FROM CATEGORIA WHERE id=?"
SQL_DELETE_CAT = "DELETE FROM CATEGORIA WHERE id=?"


SCRIPT_CATEGORIA = """
                    INSERT OR IGNORE INTO CATEGORIA(nombre) VALUES
                    ('Alimentación'),
                    ('Transporte'),
                    ('Servicios'),
                    ('Ocio'),
                    ('Otros');
                    """

class GastosRepository:
    
    def __init__(self, ruta_bd):
        self.ruta_bd = Path(ruta_bd)
    
    def _conectar(self):
        con = sqlite3.connect(self.ruta_bd)
        # Activar el soporte para claves foráneas en esta conexión
        con.execute("PRAGMA foreign_keys = ON;")
        return con
    
    def createBD(self):
        self.ruta_bd.parent.mkdir(parents=True, exist_ok=True)
        with closing(self._conectar()) as con:
            # executescript permite ejecutar bloques SQL completos
            con.executescript(SQL_CREATEBD)
            
    #--------------------CATEGORIA--------------------  
    def insertar_cat(self, nombre):
        with closing(self._conectar()) as con:
            with con:
                con.execute(SQL_INSERT_CAT, (nombre,))
        
    def _insertar_catDEFAULT(self):
        with closing(self._conectar()) as con:
            con.executescript(SCRIPT_CATEGORIA)
                
    def actualizar_cat(self, nombre, id_cat):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(SQL_UPDATE_CAT, (nombre, id_cat))
                return cursor.rowcount > 0
    
    def buscarID_cat(self, id_cat):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_READ_CAT, (id_cat,))
            return cursor.fetchone()
    
    def eliminar_cat(self, id_cat):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(SQL_DELETE_CAT, (id_cat,))
                return cursor.rowcount > 0

    #--------------------GASTOS--------------------