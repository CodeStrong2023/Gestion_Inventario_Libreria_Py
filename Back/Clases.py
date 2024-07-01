
class Articulo:
    def __init__(self, idArticulo, alto, ancho, peso, precio, tipo):
        self.idArticulo = idArticulo
        self.alto = alto
        self.ancho = ancho
        self.peso = peso
        self.precio = precio
        self.tipo = tipo
    
    def __str__(self):
        return f"Articulo(idArticulo={self.idArticulo}, alto='{self.alto}', ancho='{self.ancho}', peso='{self.peso}', precio={self.precio}, tipo='{self.tipo}')"

class Pais:
    def __init__(self, idPais, nombre):
        self.idPais = idPais
        self.nombre = nombre
    
    def __str__(self):
        return f"Pais(idPais={self.idPais}, nombre='{self.nombre}')"

class Ciudad:
    def __init__(self, idCiudad, nombre, Pais_idPais):
        self.idCiudad = idCiudad
        self.nombre = nombre
        self.Pais_idPais = Pais_idPais
    
    def __str__(self):
        return f"Ciudad(idCiudad={self.idCiudad}, nombre='{self.nombre}', Pais_idPais={self.Pais_idPais})"

class Direccion:
    def __init__(self, idDireccion, calle, numero, descripcion, Ciudad_idCiudad, Ciudad_Pais_idPais):
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
    def __init__(self, idRol, rol):
        self.idRol = idRol
        self.rol = rol
    
    def __str__(self):
        return f"Rol(idRol={self.idRol}, rol='{self.rol}')"

class Rol:
    def __init__(self,idRol=None, rol=None):
        self.idRol = idRol
        self.rol = rol
    
    def __str__(self):
        return f"Rol(idRol={self.idRol}, rol='{self.rol}')"

class Usuario:
    def __init__(self, idUsuario, nombre, apellido, correo, telefono, fechaNacimiento, imagenUsuario, Direccion_idDireccion, Rol_idRol):
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

class Empresa:
    def __init__(self, idEmpresa, nombre, telefono, correo, cuil, logoEmpresa, Direccion_idDireccion):
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
    def __init__(self, idAlmacenamiento, capacidadTotalM3, usoM3, Empresa_idEmpresa, Direccion_idDireccion):
        self.idAlmacenamiento = idAlmacenamiento
        self.capacidadTotalM3 = capacidadTotalM3
        self.usoM3 = usoM3
        self.Empresa_idEmpresa = Empresa_idEmpresa
        self.Direccion_idDireccion = Direccion_idDireccion
    
    def __str__(self):
        return (f"Almacenamiento(idAlmacenamiento={self.idAlmacenamiento}, capacidadTotalM3='{self.capacidadTotalM3}', usoM3='{self.usoM3}', "
                f"Empresa_idEmpresa={self.Empresa_idEmpresa}, Direccion_idDireccion={self.Direccion_idDireccion})")

class Envio:
    def __init__(self, idEnvio, tipo, estado, fechaDespacho, fechaEntrega, Direccion_idDireccion):
        self.idEnvio = idEnvio
        self.tipo = tipo
        self.estado = estado
        self.fechaDespacho = fechaDespacho
        self.fechaEntrega = fechaEntrega
        self.Direccion_idDireccion = Direccion_idDireccion
    
    def __str__(self):
        return (f"Envio(idEnvio={self.idEnvio}, tipo='{self.tipo}', estado='{self.estado}', fechaDespacho={self.fechaDespacho}, "
                f"fechaEntrega={self.fechaEntrega}, Direccion_idDireccion={self.Direccion_idDireccion})")

class Facturas:
    def __init__(self, idFacturas, tipo, fechaEmision, imagenFactura):
        self.idFacturas = idFacturas
        self.tipo = tipo
        self.fechaEmision = fechaEmision
        self.imagenFactura = imagenFactura
    
    def __str__(self):
        return (f"Facturas(idFacturas={self.idFacturas}, tipo='{self.tipo}', fechaEmision={self.fechaEmision}, "
                f"imagenFactura='{self.imagenFactura}')")

class Pago:
    def __init__(self, idPago, tipo, cuotas, Facturas_idFacturas, origen):
        self.idPago = idPago
        self.tipo = tipo
        self.cuotas = cuotas
        self.Facturas_idFacturas = Facturas_idFacturas
        self.origen = origen
    
    def __str__(self):
        return (f"Pago(idPago={self.idPago}, tipo='{self.tipo}', cuotas={self.cuotas}, "
                f"Facturas_idFacturas={self.Facturas_idFacturas}, origen='{self.origen}')")

class Venta:
    def __init__(self, idVenta, fechaVenta, Usuario_idUsuario, Envio_idEnvio, Articulo_idArticulo, Pago_idPago):
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
    def __init__(self, idEditorial, nombre, imagenEditorial):
        self.idEditorial = idEditorial
        self.nombre = nombre
        self.imagenEditorial = imagenEditorial
    
    def __str__(self):
        return f"Editorial(idEditorial={self.idEditorial}, nombre='{self.nombre}', imagenEditorial='{self.imagenEditorial}')"

class Proveedor:
    def __init__(self, idProveedor, nombre, telefono, contactoPrincipal):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.telefono = telefono
        self.contactoPrincipal = contactoPrincipal
    
    def __str__(self):
        return (f"Proveedor(idProveedor={self.idProveedor}, nombre='{self.nombre}', telefono='{self.telefono}', "
                f"contactoPrincipal='{self.contactoPrincipal}')")

class Devolucion:
    def __init__(self, idDevolucion, motivo, fechaDevolucion, cantidad, Pago_idPago):
        self.idDevolucion = idDevolucion
        self.motivo = motivo
        self.fechaDevolucion = fechaDevolucion
        self.cantidad = cantidad
        self.Pago_idPago = Pago_idPago
    
    def __str__(self):
        return (f"Devolucion(idDevolucion={self.idDevolucion}, motivo='{self.motivo}', fechaDevolucion={self.fechaDevolucion}, "
                f"cantidad={self.cantidad}, Pago_idPago={self.Pago_idPago})")

class Genero:
    def __init__(self, idgenero, nombre):
        self.idgenero = idgenero
        self.nombre = nombre
    
    def __str__(self):
        return f"Genero(idgenero={self.idgenero}, nombre='{self.nombre}')"

class Libro:
    def __init__(self, idLibro, titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, Articulo_idArticulo, genero_idgenero, Editorial_idEditorial):
        self.idLibro = idLibro
        self.titulo = titulo
        self.idioma = idioma
        self.tapa = tapa
        self.año = año
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima
        self.descripcion = descripcion
        self.imagen_tapa = imagen_tapa
        self.Articulo_idArticulo = Articulo_idArticulo
        self.genero_idgenero = genero_idgenero
        self.Editorial_idEditorial = Editorial_idEditorial
    
    def __str__(self):
        return (f"Libro(idLibro={self.idLibro}, titulo='{self.titulo}', idioma='{self.idioma}', tapa='{self.tapa}', año={self.año}, "
                f"isbn='{self.isbn}', paginas='{self.paginas}', edicion='{self.edicion}', edad_minima={self.edad_minima}, "
                f"edad_maxima={self.edad_maxima}, descripcion='{self.descripcion}', imagen_tapa='{self.imagen_tapa}', "
                f"Articulo_idArticulo={self.Articulo_idArticulo}, genero_idgenero={self.genero_idgenero}, "
                f"Editorial_idEditorial={self.Editorial_idEditorial})")

class Autor:
    def __init__(self, idAutor, nombre, apellido, imagenAutor):
        self.idAutor = idAutor
        self.nombre = nombre
        self.apellido = apellido
        self.imagenAutor = imagenAutor
    
    def __str__(self):
        return f"Autor(idAutor={self.idAutor}, nombre='{self.nombre}', apellido='{self.apellido}', imagenAutor='{self.imagenAutor}')"

class Autor:
    def __init__(self, idAutor, nombre, apellido, imagenAutor):
        self.idAutor = idAutor
        self.nombre = nombre
        self.apellido = apellido
        self.imagenAutor = imagenAutor
    
    def __str__(self):
        return f"Autor(idAutor={self.idAutor}, nombre='{self.nombre}', apellido='{self.apellido}', imagenAutor='{self.imagenAutor}')"

class Revista:
    def __init__(self, idRevista, titulo, numero, anio, mes, dia, Articulo_idArticulo, Editorial_idEditorial, genero_idgenero):
        self.idRevista = idRevista
        self.titulo = titulo
        self.numero = numero
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.Articulo_idArticulo = Articulo_idArticulo
        self.Editorial_idEditorial = Editorial_idEditorial
        self.genero_idgenero = genero_idgenero
    
    def __str__(self):
        return (f"Revista(idRevista={self.idRevista}, titulo='{self.titulo}', numero={self.numero}, anio={self.anio}, mes={self.mes}, "
                f"dia={self.dia}, Articulo_idArticulo={self.Articulo_idArticulo}, Editorial_idEditorial={self.Editorial_idEditorial}, "
                f"genero_idgenero={self.genero_idgenero})")
