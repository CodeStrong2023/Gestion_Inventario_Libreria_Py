from Backend.controllers.controllers import Crud
from Backend.entities.entities import Articulo

class ArticuloService:
    def __init__(self, conn):
        self.conn = conn
        
    def crear_articulo(self, alto, ancho, peso, precio, tipo):
        nuevo_articulo = Articulo(
            alto=alto,
            ancho=ancho,
            peso=peso,
            precio=precio,
            tipo=tipo
        )
        Crud.crear(nuevo_articulo, self.conn)
        return nuevo_articulo
    
    def actualizar_articulo(self, idArticulo, alto, ancho, peso, precio, tipo):
        nuevo_articulo = Articulo(
            idArticulo=idArticulo,
            alto=alto,
            ancho=ancho,
            peso=peso,
            precio=precio,
            tipo=tipo
        )
        Crud.actualizar(Articulo, self.conn, nuevo_articulo)
        return nuevo_articulo
    
    def buscar_articulo(self, idArticulo):
        return Crud.leer(Articulo, self.conn, idArticulo)
    
    def buscar_articulos(self):
        return Crud.leerTodos(Articulo, self.conn)
    
    def eliminar_articulo(self, idArticulo):
        Crud.eliminar(Articulo, self.conn, idArticulo)

    def buscar_articulos_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Articulo, self.conn, criterio_busqueda)
    
    
    
    
    