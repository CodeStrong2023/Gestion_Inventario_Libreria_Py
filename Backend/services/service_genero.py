from Backend.controllers.controllers import Crud
from Backend.entities.entities import Genero


class GeneroService:
    def __init__(self, conn):
        self.conn = conn

    def crear_genero(self, nombre):
        nuevo_genero = Genero(
            nombre=nombre
        )
        Crud.crear(nuevo_genero, self.conn)
        return nuevo_genero

    def actualizar_genero(self, idGenero, nombre):
        nuevo_genero = Genero(
            idGenero=idGenero,
            nombre=nombre
        )
        Crud.actualizar(Genero, self.conn, nuevo_genero)
        return nuevo_genero

    def buscar_genero(self, idGenero):
        return Crud.leer(Genero, self.conn, idGenero)
    
    def buscar_generos(self):
        return Crud.leerTodos(Genero, self.conn)
    
    def eliminar_genero(self, idGenero):
        Crud.eliminar(Genero, self.conn, idGenero)

    def buscar_generos_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Genero, self.conn, criterio_busqueda)

