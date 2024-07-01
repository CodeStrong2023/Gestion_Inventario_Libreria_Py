from Backend.controllers.controllers import Crud
from Backend.entities.entities import Devolucion

class DevolucionService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_devolucion(self, motivo, fechaDevolucion, cantidad, pago):
        nueva_devolucion = Devolucion(
            motivo=motivo,
            fechaDevolucion=fechaDevolucion,
            cantidad=cantidad,
            Pago_idPago=pago
        )
        Crud.crear(nueva_devolucion, self.conn)
        return nueva_devolucion
    
    def actualizar_devolucion(self, idDevolucion, motivo, fechaDevolucion, cantidad, pago):
        nueva_devolucion = Devolucion(
            idDevolucion=idDevolucion,
            motivo=motivo,
            fechaDevolucion=fechaDevolucion,
            cantidad=cantidad,
            Pago_idPago=pago
        )
        Crud.actualizar(Devolucion, self.conn, nueva_devolucion)
        return nueva_devolucion
    
    def buscar_devolucion(self, idDevolucion):
        return Crud.leer(Devolucion, self.conn, idDevolucion)
    
    def buscar_devoluciones(self):
        return Crud.leerTodos(Devolucion, self.conn)
    
    def eliminar_devolucion(self, idDevolucion):
        Crud.eliminar(Devolucion, self.conn, idDevolucion)

    def buscar_devoluciones_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Devolucion, self.conn, criterio_busqueda)