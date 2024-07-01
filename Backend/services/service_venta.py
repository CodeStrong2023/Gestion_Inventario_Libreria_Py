from Backend.controllers.controllers import Crud
from Backend.entities.entities import Venta

class VentaService:
    def __init__(self, conn):
        self.conn = conn
    
    def crear_venta(self, fecha, usuario, envio, articulo, pago ):
        nueva_venta = Venta(
            fechaVenta=fecha,
            Envio_idEnvio=envio,
            Articulo_idArticulo=articulo,
            Pago_idPago=pago
        )
        Crud.crear(nueva_venta, self.conn)
        return nueva_venta
    
    def actualizar_venta(self, idVenta, fechaVenta, Envio_idEnvio, Articulo_idArticulo, PagoID ):
        venta = Venta(
            idVenta=idVenta,
            fechaVenta=fechaVenta,
            Envio_idEnvio=Envio_idEnvio,
            Articulo_idArticulo=Articulo_idArticulo,
            Pago_idPago=PagoID
        )
        Crud.actualizar(venta, self.conn)
        return venta
    
    def buscar_venta(self, idVenta):
        return Crud.leer(Venta, self.conn, idVenta)
    
    def buscar_ventas(self):
        return Crud.leerTodos(Venta, self.conn)
    
    def eliminar_venta(self, idVenta):
        Crud.eliminar(Venta, self.conn, idVenta)

    def buscar_ventas_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Venta, self.conn, criterio_busqueda)
    
    