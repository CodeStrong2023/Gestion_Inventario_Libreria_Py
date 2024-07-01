from Backend.controllers.controllers import Crud
from Backend.entities.entities import Almacenamiento

class AlmacenamientoService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_almacenamiento(self, capacidadTotalM3=0, usoM3=0, Empresa_idEmpresa=None, Direccion_idDireccion=None):
        nuevo_almacenamiento = Almacenamiento(
            capacidadTotalM3 = capacidadTotalM3,
            usoM3 = usoM3,
            Empresa_idEmpresa = Empresa_idEmpresa,
            Direccion_idDireccion = Direccion_idDireccion
        )
        Crud.crear(nuevo_almacenamiento, self.conn)
        return nuevo_almacenamiento
    
    def buscar_almacenamiento(self, idAlmacenamiento):
        return Crud.leer(Almacenamiento, self.conn, idAlmacenamiento)

    def buscar_almacenamientos(self):
        return Crud.leerTodos(Almacenamiento, self.conn)

    def actualizar_almacenamiento(self, idAlmacenamiento, capacidadTotalM3, usoM3, Empresa_idEmpresa, Direccion_idDireccion):
        almacenamiento = self.buscar_almacenamiento(idAlmacenamiento)
        if almacenamiento:       
            almacenamiento.capacidadTotalM3 = capacidadTotalM3
            almacenamiento.usoM3 = usoM3
            almacenamiento.Empresa_idEmpresa = Empresa_idEmpresa
            almacenamiento.Direccion_idDireccion = Direccion_idDireccion
            Crud.actualizar(almacenamiento, self.conn)
            return almacenamiento
        return None

    def eliminar_almacenamiento(self, idAlmacenamiento):
        Crud.eliminar(Almacenamiento, self.conn, idAlmacenamiento)

    def buscar_almacenamientos_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Almacenamiento, self.conn, criterio_busqueda)
