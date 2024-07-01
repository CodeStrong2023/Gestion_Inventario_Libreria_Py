from Backend.controllers.controllers import Crud
from Backend.entities.entities import Factura



class FacturaService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_factura(self, tipo, fechaEmicion, imagenFactura):
        nueva_factura = Factura(
            tipo=tipo,
            fechaEmision=fechaEmicion,
            imagenFactura=imagenFactura,
        )
        Crud.crear(nueva_factura, self.conn)
        return nueva_factura
    
    def actualizar_factura(self, idFactura, tipo, fechaEmicion, imagenFactura):
        nueva_factura = Factura(
            idFacturas=idFactura,
            tipo=tipo,
            fechaEmision=fechaEmicion,
            imagenFactura=imagenFactura,
        )
        Crud.actualizar(Factura, self.conn, nueva_factura)
        
        return nueva_factura
    
    def buscar_factura(self, idFactura):
        return Crud.leer(Factura, self.conn, idFactura)
    
    def buscar_facturas(self):
        return Crud.leerTodos(Factura, self.conn)
    
    def eliminar_factura(self, idFactura):
        Crud.eliminar(Factura, self.conn, idFactura)

    def buscar_facturas_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Factura, self.conn, criterio_busqueda)