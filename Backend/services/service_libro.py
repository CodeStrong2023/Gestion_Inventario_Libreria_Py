import sqlite3
from Backend.controllers.controllers import Crud
from Backend.entities.entities import Libro

class LibroService:
    def __init__(self, conn):
        self.conn = conn

    def crear_libro(self, titulo, idioma, tapa, anio, isbn, paginas, edicion, edad_minima, edad_maxima, descipcion, imagen_tapa, Articulo_idArticulo, Genero_idGenero,Editorial_idEditorial):
        nuevo_libro = Libro(
            titulo=titulo,
            idioma=idioma,
            tapa=tapa,
            anio=anio,
            isbn=isbn,
            paginas=paginas,
            edicion=edicion,
            edad_minima=edad_minima,
            edad_maxima=edad_maxima,
            descripcion=descipcion,
            imagen_tapa=imagen_tapa,
            Articulo_idArticulo=Articulo_idArticulo,
            Genero_idGenero=Genero_idGenero,
            Editorial_idEditorial=Editorial_idEditorial
        )
        Crud.crear(nuevo_libro, self.conn)
        return nuevo_libro

    def actualizar_libro(self, idLibro, titulo, idioma, tapa, anio, isbn, paginas, edicion, edad_minima, edad_maxima, descipcion, imagen_tapa, Articulo_idArticulo, Genero_idGenero,Editorial_idEditorial):
        nuevo_libro = Libro(
            idLibro = idLibro,
            titulo=titulo,
            idioma=idioma,
            tapa=tapa,
            anio=anio,
            isbn=isbn,
            paginas=paginas,
            edicion=edicion,
            edad_minima=edad_minima,
            edad_maxima=edad_maxima,
            descripcion=descipcion,
            imagen_tapa=imagen_tapa,
            Articulo_idArticulo=Articulo_idArticulo,
            Genero_idGenero=Genero_idGenero,
            Editorial_idEditorial=Editorial_idEditorial
        )
        Crud.actualizar(Libro, self.conn, nuevo_libro)
        return nuevo_libro
    
    def buscar_libro(self, idLibro):
        return Crud.leer(Libro, self.conn, idLibro)
    
    def buscar_libros(self):
        return Crud.leerTodos(Libro, self.conn)
    
    def eliminar_libro(self, idLibro):
        Crud.eliminar(Libro, self.conn, idLibro)

    def buscar_libros_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Libro, self.conn, criterio_busqueda)
    
    def leer_libros_articulo(self, idArticulo):
        sql_select_libros_articulo = "SELECT * FROM Libro WHERE Articulo_idArticulo = ?"

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_select_libros_articulo, (idArticulo,))
            row = cursor.fetchone()
            if row:
                attributes = dict(zip([column[0] for column in cursor.description], row))
                return Libro(**attributes)
            else:
                return None
        
        except sqlite3.Error as e:
            print(f"Error al leer los datos: {e}")
            return None