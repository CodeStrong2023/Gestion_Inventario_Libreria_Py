import sqlite3
from Backend.controllers.controllers import Crud
from Backend.entities.entities import Revista

class RevistaService:
    def __init__(self, conn):
        self.conn = conn
        

    def crear_revista(self, titulo, numero, anio, mes, dia, Articulo_idArticulo, Editorial_idEditorial, Genero_idGenero):
        nuevo_revista = Revista(
            titulo=titulo,
            numero=numero,
            anio=anio,
            mes=mes,
            dia=dia,
            Articulo_idArticulo=Articulo_idArticulo,
            Editorial_idEditorial=Editorial_idEditorial,
            Genero_idGenero=Genero_idGenero
        )
        Crud.crear(nuevo_revista, self.conn)
        return nuevo_revista
    
    def actualizar_revista(self, idRevista, titulo, numero, anio, mes, dia, Articulo_idArticulo, Editorial_idEditorial, Genero_idGenero):
        nueva_revista = Revista(
            idRevista = idRevista,
            titulo=titulo,
            numero=numero,
            anio=anio,
            mes=mes,
            dia=dia,
            Articulo_idArticulo=Articulo_idArticulo,
            Editorial_idEditorial=Editorial_idEditorial,
            Genero_idGenero=Genero_idGenero
        )
        Crud.actualizar(Revista, self.conn, nueva_revista)

    def buscar_revista(self, idRevista):
        return Crud.leer(Revista, self.conn, idRevista)
    
    def buscar_revistas(self):
        return Crud.leerTodos(Revista, self.conn)
    
    def eliminar_revista(self, idRevista):
        Crud.eliminar(Revista, self.conn, idRevista)

    def buscar_revistas_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Revista, self.conn, criterio_busqueda)
    
    def leer_revistas_articulo(self, idArticulo):
        sql_select_revistas_articulo = "SELECT * FROM Revista WHERE Articulo_idArticulo = ?"

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_select_revistas_articulo, (idArticulo,))
            row = cursor.fetchone()
            if row:
                attributes = dict(zip([column[0] for column in cursor.description], row))
                return Revista(**attributes)
            else:
                return None
        
        except sqlite3.Error as e:
            print(f"Error al leer los datos: {e}")
            return None