from database.connection import Connection
from Back.CRUD import Crud
from Back.Clases import Rol

class PruebaCrud:
    @staticmethod
    def pruebaCrear(conn):             
        rol = Rol(idRol=None,rol='Prueba')
        Crud.crear(rol, conn)
        rolLeido=Crud.leer(Rol, conn, rol.idRol)
        print("Rol creado correctamente")
        print(rolLeido)
        
    def pruebaLeer(conn):
        rolLeido2 = Crud.leer(Rol, conn, 1)
        if rolLeido2:
            print("Rol leído correctamente")
            print(rolLeido2)
        else:
            print("No se encontró ningún rol con ID 1")
            
            
    @staticmethod
    def pruebaActualizar(conn):
        rol = Rol(idRol=1,rol='Prueba2')
        Crud.actualizar(rol, conn)
        rolLeido=Crud.leer(Rol, conn, rol.idRol)
        print("Rol actualizado correctamente")
        print(rolLeido)
    @staticmethod    
    def pruebaEliminar(conn):
        Crud.eliminar(Rol, conn, 1)
        rolLeido=Crud.leer(Rol, conn, 1)
        print("Rol eliminado correctamente")
        print(rolLeido)
    @staticmethod    
    def pruebaLeerTodos(conn):
        roles=Crud.leerTodos(Rol, conn)
        print("Roles leidos correctamente")
        print(roles)