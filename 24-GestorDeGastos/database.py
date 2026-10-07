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
                    fecha DATE NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES CATEGORIA(id) ON DELETE RESTRICT
                );
                """

SQL_INSERT_CAT = "INSERT INTO CATEGORIA(nombre) VALUES (?)"
SQL_UPDATE_CAT = "UPDATE CATEGORIA SET nombre=? WHERE id=?"
SQL_READ_CAT = "SELECT id FROM CATEGORIA WHERE nombre=?"
SQL_READ_ID_CAT = "SELECT nombre FROM CATEGORIA WHERE id=?"
SQL_DELETE_CAT = "DELETE FROM CATEGORIA WHERE id=?"


SCRIPT_CATEGORIA = """
                    INSERT OR IGNORE INTO CATEGORIA(nombre) VALUES
                    ('Alimentación'),
                    ('Transporte'),
                    ('Servicios'),
                    ('Ocio'),
                    ('Otros');
                    """# OR IGNORE INTO-> al encontrar cualquier
                       #error(Menos el de los foraneos **
                       # Para eso esta el DELETE ON y el PRAGMA**), lo quita SILENCIOSAMENTE(No lanza error)

SQL_FILTRO_CATEGORIA ="""
                    SELECT * FROM CATEGORIA
                    WHERE nombre = ?
                    """
SQL_FILTRO_CATEGORIA_TODOS ="""
                    SELECT * FROM CATEGORIA
                    """


SQL_INSERT_GASTO = "INSERT INTO GASTO(descripcion, monto, categoria_id, fecha) VALUES (?,?,?,?)"
SQL_READ_GASTO= "SELECT * FROM GASTO WHERE nombre=?"
SQL_DELETE_GASTO = "DELETE FROM GASTO WHERE id=?"
SQL_UPDATE_GASTO = """
                    UPDATE GASTO 
                    SET descripcion=?, monto=?, categoria_id=?, fecha=? 
                    WHERE id=?
                    """
SQL_FILTRO_GASTO ="""
                    SELECT g.id, g.descripcion, g.monto, c.nombre, g.fecha
                    FROM GASTO g
                    INNER JOIN CATEGORIA c ON g.categoria_id = c.id
                    WHERE g.categoria_id = ?
                    ORDER BY g.fecha DESC
                    """
                    
SQL_FILTRO_GASTO_MONTO = """SELECT SUM(gat.monto) 
                        FROM CATEGORIA cat INNER JOIN GASTO gat
                        on cat.id = gat.categoria_id 
                        WHERE nombre = ?
                        """
SQL_FILTRO_GASTO_MONTO_TODOS = """SELECT SUM(gat.monto) 
                        FROM CATEGORIA cat INNER JOIN GASTO gat
                        on cat.id = gat.categoria_id 
                        """
SQL_FILTRO_MESES_GASTO="""
                        SELECT DISTINCT gat.id, gat.descripcion, gat.monto, gat.categoria_id, gat.fecha
                        FROM GASTO gat
                        ORDER BY gat.fecha DESC
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
            con.executescript(SQL_CREATEBD)
            
            cursor = con.execute("SELECT COUNT(*) FROM CATEGORIA")
            total = cursor.fetchone()[0]
            
            if total == 0:
                con.executescript(SCRIPT_CATEGORIA)
            
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
    
    def buscarNombre_cat(self, nombre):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_READ_CAT, (nombre,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        
    def buscarID_cat(self, id_cat):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_READ_ID_CAT, (id_cat,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        
    def eliminar_cat(self, id_cat):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(SQL_DELETE_CAT, (id_cat,))
                return cursor.rowcount > 0

    def getdatos(self):
        with closing(self._conectar()) as con:
            cursor = con.execute("SELECT * FROM CATEGORIA")
            return cursor.fetchall()
        
    def filtroCategoria(self,nombre):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_CATEGORIA, (nombre,))
            return cursor.fetchall() 
        
    def filtroCategoriaTODOS(self):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_CATEGORIA_TODOS)
            return cursor.fetchall()       
        
    #--------------------GASTOS--------------------
    
    def insertar_gasto(self, descripcion, monto, categoria_id, fecha):
        with closing(self._conectar()) as con:
            with con:
                con.execute(SQL_INSERT_GASTO, (descripcion, monto, categoria_id, fecha,))
                   
    def actualizar_gasto(self, descripcion, monto, categoria_id, fecha, id_cat):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(SQL_UPDATE_GASTO, (descripcion, monto, categoria_id, fecha, id_cat,))
                return cursor.rowcount > 0
    
    def buscarID_gasto(self, id_cat):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_READ_CAT, (id_cat,))
            return cursor.fetchone()
    
    def eliminar_gasto(self, id_gasto):
        with closing(self._conectar()) as con:
            with con:
                cursor = con.execute(SQL_DELETE_GASTO, (id_gasto,))
                return cursor.rowcount > 0

    def getdatosGASTO(self):
        with closing(self._conectar()) as con:
            cursor = con.execute("SELECT * FROM GASTO")
            return cursor.fetchall()

    def filtroGasto(self,id_gasto):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_GASTO, (id_gasto,))
            return cursor.fetchall()
        
    def filtroGastoMONTO(self,nombre):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_GASTO_MONTO, (nombre,))
            return cursor.fetchall()[0]
        
    def filtroGastoMONTO_TODOS(self):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_GASTO_MONTO_TODOS)
            return cursor.fetchall()[0]
        
    def filtro_meses_gastos(self):
        with closing(self._conectar()) as con:
            cursor = con.execute(SQL_FILTRO_MESES_GASTO)
            return cursor.fetchall()