from Backend.controllers.controllers import Crud
from Backend.entities.entities import Proveedor

class ProveedorService:
    def __init__(self, conn):
        self.conn = conn
    
    def crear_provedor(self, nombre, telefono, contactoPrincipal):
        nuevo_provedor = Proveedor(
            nombre=nombre,
            telefono=telefono,
            contactoPrincipal=contactoPrincipal
        )
        Crud.crear(nuevo_provedor, self.conn)
        return nuevo_provedor
    
    def actualizar_proveedor(self, idProveedor, nombre, telefono, contactoPrincipal):
        nuevo_proveedor = Proveedor(
            idProveedor = idProveedor,
            nombre = nombre,
            telefono = telefono,
            contactoPrincipal = contactoPrincipal
        )
        Crud.actualizar(Proveedor, self.conn, nuevo_proveedor)
        
    def buscar_proveedor(self, idProveedor):
        return Crud.leer(Proveedor, self.conn, idProveedor)
    
    def buscar_proveedores(self):
        return Crud.leerTodos(Proveedor, self.conn)
    
    def eliminar_proveedor(self, idProveedor):
        Crud.eliminar(Proveedor, self.conn, idProveedor)

    def buscar_proveedores_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Proveedor, self.conn, criterio_busqueda)