
class Articulo:
    def __init__(self, idArticulo=None, alto=0, ancho=0, peso=0, precio=0.0, tipo=""):
        self.idArticulo = idArticulo
        self.alto = alto
        self.ancho = ancho
        self.peso = peso
        self.precio = precio
        self.tipo = tipo
    
    def __str__(self):
        return f"Articulo(idArticulo={self.idArticulo}, alto='{self.alto}', ancho='{self.ancho}', peso='{self.peso}', precio={self.precio}, tipo='{self.tipo}')"

class Pais:
    def __init__(self, idPais=None, nombre=""):
        self.idPais = idPais
        self.nombre = nombre
    
    def __str__(self):
        return f"Pais(idPais={self.idPais}, nombre='{self.nombre}')"

class Ciudad:
    def __init__(self, idCiudad=None, nombre="", Pais_idPais=None):
        self.idCiudad = idCiudad
        self.nombre = nombre
        self.Pais_idPais = Pais_idPais
    
    def __str__(self):
        return f"Ciudad(idCiudad={self.idCiudad}, nombre='{self.nombre}', Pais_idPais={self.Pais_idPais})"

class Direccion:
    def __init__(self, idDireccion=None, calle="", numero="", descripcion="", Ciudad_idCiudad=None, Ciudad_Pais_idPais=None):
        self.idDireccion = idDireccion
        self.calle = calle
        self.numero = numero
        self.descripcion = descripcion
        self.Ciudad_idCiudad = Ciudad_idCiudad
        self.Ciudad_Pais_idPais = Ciudad_Pais_idPais


    
    def __str__(self):
        return (f"Direccion(idDireccion={self.idDireccion}, calle='{self.calle}', numero='{self.numero}', "
                f"descripcion='{self.descripcion}', Ciudad_idCiudad={self.Ciudad_idCiudad}, "
                f"Ciudad_Pais_idPais={self.Ciudad_Pais_idPais})")

class Rol:
    def __init__(self, idRol=None, rol=""):
        self.idRol = idRol
        self.rol = rol
    
    def __str__(self):
        return f"Rol(idRol={self.idRol}, rol='{self.rol}')"

class Usuario:
    def __init__(self, idUsuario=None, nombre="", apellido="", correo="", telefono="", fechaNacimiento="1900-01-01", imagenUsuario="", Direccion_idDireccion=None, Rol_idRol=None):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.imagenUsuario = imagenUsuario
        self.Direccion_idDireccion = Direccion_idDireccion
        self.Rol_idRol = Rol_idRol
    
    def __str__(self):
        return (f"Usuario(idUsuario={self.idUsuario}, nombre='{self.nombre}', apellido='{self.apellido}', correo='{self.correo}', "
                f"telefono='{self.telefono}', fechaNacimiento={self.fechaNacimiento}, imagenUsuario='{self.imagenUsuario}', "
                f"Direccion_idDireccion={self.Direccion_idDireccion}, Rol_idRol={self.Rol_idRol})")
        
@staticmethod 
class Compra:
    def __init__(self, idCompra=None, Almacenamiento_idAlmacenamiento=None, Articulo_idArticulo=None, fecha="1900-01-01", cantidad=0, precioUnitario=0.0, Pago_idPago=None, Proveedor_idProveedor=None):
        self.idCompra = idCompra
        self.Almacenamiento_idAlmacenamiento = Almacenamiento_idAlmacenamiento
        self.Articulo_idArticulo = Articulo_idArticulo
        self.fecha = fecha
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.Pago_idPago = Pago_idPago
        self.Proveedor_idProveedor = Proveedor_idProveedor

    def __str__(self):
        return (f"Compra(idCompra={self.idCompra}, Almacenamiento_idAlmacenamiento={self.Almacenamiento_idAlmacenamiento}, "
                f"Articulo_idArticulo={self.Articulo_idArticulo}, fecha={self.fecha}, cantidad={self.cantidad}, "
                f"precioUnitario={self.precioUnitario}, Pago_idPago={self.Pago_idPago}, Proveedor_idProveedor={self.Proveedor_idProveedor})")


class Empresa:
    def __init__(self, idEmpresa=None, nombre="", telefono="", correo="", cuil="", logoEmpresa="", Direccion_idDireccion=None):
        self.idEmpresa = idEmpresa
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.cuil = cuil
        self.logoEmpresa = logoEmpresa
        self.Direccion_idDireccion = Direccion_idDireccion
    
    def __str__(self):
        return (f"Empresa(idEmpresa={self.idEmpresa}, nombre='{self.nombre}', telefono='{self.telefono}', correo='{self.correo}', "
                f"cuil={self.cuil}, logoEmpresa='{self.logoEmpresa}', Direccion_idDireccion={self.Direccion_idDireccion})")

class Almacenamiento:
    def __init__(self, idAlmacenamiento=None, capacidadTotalM3=0, usoM3=0, Empresa_idEmpresa=None, Direccion_idDireccion=None):
        self.idAlmacenamiento = idAlmacenamiento
        self.capacidadTotalM3 = capacidadTotalM3
        self.usoM3 = usoM3
        self.Empresa_idEmpresa = Empresa_idEmpresa
        self.Direccion_idDireccion = Direccion_idDireccion
    
    def __str__(self):
        return (f"Almacenamiento(idAlmacenamiento={self.idAlmacenamiento}, capacidadTotalM3='{self.capacidadTotalM3}', usoM3='{self.usoM3}', "
                f"Empresa_idEmpresa={self.Empresa_idEmpresa}, Direccion_idDireccion={self.Direccion_idDireccion})")

class Envio:
    def __init__(self, idEnvio=None, tipo="", estado="", fechaDespacho="1900-01-01", fechaEntrega="1900-01-01", Direccion_idDireccion=None):
        self.idEnvio = idEnvio
        self.tipo = tipo
        self.estado = estado
        self.fechaDespacho = fechaDespacho
        self.fechaEntrega = fechaEntrega
        self.Direccion_idDireccion = Direccion_idDireccion
    
    def __str__(self):
        return (f"Envio(idEnvio={self.idEnvio}, tipo='{self.tipo}', estado='{self.estado}', fechaDespacho={self.fechaDespacho}, "
                f"fechaEntrega={self.fechaEntrega}, Direccion_idDireccion={self.Direccion_idDireccion})")

class Factura:
    def __init__(self, idFactura=None, tipo="", fechaEmision="1900-01-01", imagenFactura=""):
        self.idFactura = idFactura
        self.tipo = tipo
        self.fechaEmision = fechaEmision
        self.imagenFactura = imagenFactura
    
    def __str__(self):
        return (f"Factura(idFactura={self.idFactura}, tipo='{self.tipo}', fechaEmision={self.fechaEmision}, "
                f"imagenFactura='{self.imagenFactura}')")

class Pago:
    def __init__(self, idPago=None, tipo="", cuotas=0, Factura_idFactura=None, origen=""):
        self.idPago = idPago
        self.tipo = tipo
        self.cuotas = cuotas
        self.Factura_idFactura = Factura_idFactura
        self.origen = origen
    
    def __str__(self):
        return (f"Pago(idPago={self.idPago}, tipo='{self.tipo}', cuotas={self.cuotas}, "
                f"Factura_idFactura={self.Factura_idFactura}, origen='{self.origen}')")

class Venta:
    def __init__(self, idVenta=None, fechaVenta="1900-01-01", Usuario_idUsuario=None, Envio_idEnvio=None, Articulo_idArticulo=None, Pago_idPago=None):
        self.idVenta = idVenta
        self.fechaVenta = fechaVenta
        self.Usuario_idUsuario = Usuario_idUsuario
        self.Envio_idEnvio = Envio_idEnvio
        self.Articulo_idArticulo = Articulo_idArticulo
        self.Pago_idPago = Pago_idPago
    
    def __str__(self):
        return (f"Venta(idVenta={self.idVenta}, fechaVenta={self.fechaVenta}, Usuario_idUsuario={self.Usuario_idUsuario}, "
                f"Envio_idEnvio={self.Envio_idEnvio}, Articulo_idArticulo={self.Articulo_idArticulo}, Pago_idPago={self.Pago_idPago})")

class Editorial:
    def __init__(self, idEditorial=None, nombre="", imagenEditorial=""):
        self.idEditorial = idEditorial
        self.nombre = nombre
        self.imagenEditorial = imagenEditorial
    
    def __str__(self):
        return f"Editorial(idEditorial={self.idEditorial}, nombre='{self.nombre}', imagenEditorial='{self.imagenEditorial}')"

class Proveedor:
    def __init__(self, idProveedor=None, nombre="", telefono="", contactoPrincipal=""):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.telefono = telefono
        self.contactoPrincipal = contactoPrincipal
    
    def __str__(self):
        return (f"Proveedor(idProveedor={self.idProveedor}, nombre='{self.nombre}', telefono='{self.telefono}', "
                f"contactoPrincipal='{self.contactoPrincipal}')")

class Devolucion:
    def __init__(self, idDevolucion=None, motivo="", fechaDevolucion="1900-01-01", cantidad=0, Pago_idPago=None):
        self.idDevolucion = idDevolucion
        self.motivo = motivo
        self.fechaDevolucion = fechaDevolucion
        self.cantidad = cantidad
        self.Pago_idPago = Pago_idPago
    
    def __str__(self):
        return (f"Devolucion(idDevolucion={self.idDevolucion}, motivo='{self.motivo}', fechaDevolucion={self.fechaDevolucion}, "
                f"cantidad={self.cantidad}, Pago_idPago={self.Pago_idPago})")

class Genero:
    def __init__(self, idGenero=None, nombre=""):
        self.idGenero = idGenero
        self.nombre = nombre
    
    def __str__(self):
        return f"Genero(idGenero={self.idGenero}, nombre='{self.nombre}')"

class Libro:
    def __init__(self, idLibro=None, titulo="", idioma="", tapa="", anio="", isbn="", paginas="", edicion="", edad_minima="", edad_maxima="", descripcion="", imagen_tapa="", Articulo_idArticulo=None, Genero_idGenero=None, Editorial_idEditorial=None):
        self.idLibro = idLibro
        self.titulo = titulo
        self.idioma = idioma
        self.tapa = tapa
        self.anio = anio
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima
        self.descripcion = descripcion
        self.imagen_tapa = imagen_tapa
        self.Articulo_idArticulo = Articulo_idArticulo
        self.Genero_idGenero = Genero_idGenero
        self.Editorial_idEditorial = Editorial_idEditorial
    
    def __str__(self):
        return (f"Libro(idLibro={self.idLibro}, titulo='{self.titulo}', idioma='{self.idioma}', tapa='{self.tapa}', año={self.anio}, "
                f"isbn='{self.isbn}', paginas='{self.paginas}', edicion='{self.edicion}', edad_minima={self.edad_minima}, "
                f"edad_maxima={self.edad_maxima}, descripcion='{self.descripcion}', imagen_tapa='{self.imagen_tapa}', "
                f"Articulo_idArticulo={self.Articulo_idArticulo}, Genero_idGenero={self.Genero_idGenero}, "
                f"Editorial_idEditorial={self.Editorial_idEditorial})")

class Autor:
    def __init__(self, idAutor=None, nombre="", apellido="", imagenAutor=""):
        self.idAutor = idAutor
        self.nombre = nombre
        self.apellido = apellido
        self.imagenAutor = imagenAutor
    
    def __str__(self):
        return f"Autor(idAutor={self.idAutor}, nombre='{self.nombre}', apellido='{self.apellido}', imagenAutor='{self.imagenAutor}')"


class Revista:
    def __init__(self, idRevista=None, titulo="", numero="", anio="", mes="", dia="", Articulo_idArticulo=None, Editorial_idEditorial=None, Genero_idGenero=None):
        self.idRevista = idRevista
        self.titulo = titulo
        self.numero = numero
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.Articulo_idArticulo = Articulo_idArticulo
        self.Editorial_idEditorial = Editorial_idEditorial
        self.Genero_idGenero = Genero_idGenero
    
    def __str__(self):
        return (f"Revista(idRevista={self.idRevista}, titulo='{self.titulo}', numero={self.numero}, anio={self.anio}, mes={self.mes}, "
                f"dia={self.dia}, Articulo_idArticulo={self.Articulo_idArticulo}, Editorial_idEditorial={self.Editorial_idEditorial}, "
                f"Genero_idGenero={self.Genero_idGenero})")
