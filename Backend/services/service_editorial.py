from Backend.controllers.controllers import Crud
from Backend.entities.entities import Editorial

class EditorialService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_editorial(self, nombre, imagenEditorial):
        nueva_editorial = Editorial(
            nombre=nombre,
            imagenEditorial=imagenEditorial
        )
        Crud.crear(nueva_editorial, self.conn)
        return nueva_editorial
    
    def actualizar_editorial(self, idEditorial, nombre, imagenEditorial):
        editorial = self.buscar_editorial(idEditorial)
        nueva_editorial = Editorial(
            idEditorial=idEditorial,
            nombre=nombre,
            imagenEditorial=imagenEditorial
        )
        if editorial:
            Crud.actualizar(Editorial, self.conn, nueva_editorial)
        return nueva_editorial

    def buscar_editorial(self, idEditorial):
        return Crud.leer(Editorial, self.conn, idEditorial)
    
    def buscar_editoriales(self):
        return Crud.leerTodos(Editorial, self.conn)
    
    def eliminar_editorial(self, idEditorial):
        Crud.eliminar(Editorial, self.conn, idEditorial)

    def buscar_editoriales_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Editorial, self.conn, criterio_busqueda)
    
