from Backend.controllers.controllers import Crud
from Backend.entities.entities import Envio, Direccion, Usuario

class EnvioService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_envio(self, tipo, estado, fechaDespacho, fechaEntrega,Direccion_idDireccion):
        nuevo_envio = Envio(
            tipo=tipo,
            estado=estado,
            fechaDespacho=fechaDespacho,
            fechaEntrega=fechaEntrega,
            Direccion_idDireccion=Direccion_idDireccion
        )
        Crud.crear(nuevo_envio, self.conn)
        return nuevo_envio
    
    def actualizar_envio(self, idEnvio, tipo, estado, fechaDespacho, fechaEntrega, Direccion_idDireccion):
        envio = self.buscar_envio(idEnvio)
        nuevo_envio = Envio(
            idEnvio=idEnvio,
            tipo=tipo,
            estado=estado,
            fechaDespacho=fechaDespacho,
            fechaEntrega=fechaEntrega,
            Direccion_idDireccion=Direccion_idDireccion
        )
        if envio:
            Crud.actualizar(Envio, self.conn, nuevo_envio)
        return nuevo_envio

    def buscar_envio(self, idEnvio):
        return Crud.leer(Envio, self.conn, idEnvio)
    
    def buscar_envios(self):
        return Crud.leerTodos(Envio, self.conn)
    
    def eliminar_envio(self, idEnvio):
        Crud.eliminar(Envio, self.conn, idEnvio)

    def buscar_envios_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Envio, self.conn, criterio_busqueda)