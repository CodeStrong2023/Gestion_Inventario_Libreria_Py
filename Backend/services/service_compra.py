from Backend.controllers.controllers import Crud
from Backend.entities.entities import Compra


class CompraService:
    def __init__(self, conn):
        self.conn = conn

    def crear_compra(self, Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario,Pago_idPago,Proveedor_idProveedor):
        nueva_compra = Compra(
            Almacenamiento_idAlmacenamiento=Almacenamiento_idAlmacenamiento,
            Articulo_idArticulo=Articulo_idArticulo,
            fecha=fecha,
            cantidad=cantidad,
            precioUnitario=precioUnitario,
            Pago_idPago=Pago_idPago,
            Proveedor_idProveedor=Proveedor_idProveedor
        )
        Crud.crear(nueva_compra, self.conn)
        return nueva_compra

    def actualizar_compra(self, idCompra, Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario,Pago_idPago,Proveedor_idProveedor):
        nueva_compra = Compra(
            idCompra=idCompra,
            Almacenamiento_idAlmacenamiento=Almacenamiento_idAlmacenamiento,
            Articulo_idArticulo=Articulo_idArticulo,
            fecha=fecha,
            cantidad=cantidad,
            precioUnitario=precioUnitario,
            Pago_idPago=Pago_idPago,
            Proveedor_idProveedor=Proveedor_idProveedor
        )
        Crud.actualizar(Compra, self.conn, nueva_compra)
        return nueva_compra
    
    def buscar_compra(self, idCompra):
        return Crud.leer(Compra, self.conn, idCompra)
    
    def buscar_compras(self):
        return Crud.leerTodos(Compra, self.conn)
    
    def eliminar_compra(self, idCompra):
        Crud.eliminar(Compra, self.conn, idCompra)

    def buscar_compras_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Compra, self.conn, criterio_busqueda)
