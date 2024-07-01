from Backend.controllers.controllers import Crud
from Backend.entities.entities import Rol

class RolService:
    def __init__(self, conn):
        self.conn = conn
    
    def crear_rol(self, rol ):
        nueva_rol = Rol(
            rol=rol
        )
        Crud.crear(nueva_rol, self.conn)
        return nueva_rol
    
    def actualizar_rol(self, idRol, rol):
        nuevo_rol = Rol(
            idRol = idRol,
            rol = rol
        )
        Crud.actualizar(Rol, self.conn, nuevo_rol)
    
    def buscar_rol(self, idRol):
        return Crud.leer(Rol, self.conn, idRol)
    
    def buscar_roless(self):
        return Crud.leerTodos(Rol, self.conn)
    
    def eliminar_rol(self, idRol):
        Crud.eliminar(Rol, self.conn, idRol)

    def buscar_roles_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Rol, self.conn, criterio_busqueda)