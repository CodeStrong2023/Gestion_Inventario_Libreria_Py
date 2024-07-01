from Backend.controllers.controllers import Crud
from Backend.entities.entities import Pago

class PagoService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_pago(self, tipo, cuotas, factura,origen):
        nuevo_pago = Pago(
            tipo=tipo,
            cuotas=cuotas,
            Facturas_idFacturas=factura,
            origen=origen
        )
        Crud.crear(nuevo_pago, self.conn)
        return nuevo_pago
    
    def actualizar_pago(self, idPago, tipo, cuotas, factura,origen):
        nuevo_pago = Pago(
            tipo=tipo,
            cuotas=cuotas,
            Facturas_idFacturas=factura,
            origen=origen
        )
        Crud.actualizar(Pago, self.conn, nuevo_pago)
        
        return nuevo_pago
    
    def buscar_pago(self, idPago):
        return Crud.leer(Pago, self.conn, idPago)
    
    def buscar_pagos(self):
        return Crud.leerTodos(Pago, self.conn)
    
    def eliminar_pago(self, idPago):
        Crud.eliminar(Pago, self.conn, idPago)

    def buscar_pagos_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Pago, self.conn, criterio_busqueda)
    