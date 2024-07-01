class CreateTables:
        
    @staticmethod
    def tablaArticulo():
        sql_create_table_Articulo = """
        CREATE TABLE IF NOT EXISTS Articulo (
            idArticulo INTEGER PRIMARY KEY AUTOINCREMENT,
            alto VARCHAR(45),
            ancho VARCHAR(45),
            peso VARCHAR(45),
            precio DOUBLE,
            tipo VARCHAR(50)
        );"""
        return sql_create_table_Articulo
    
    @staticmethod
    def tablaPais():
        sql_create_table_Pais = """
        CREATE TABLE IF NOT EXISTS Pais (
            idPais INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45)
        );"""
        return sql_create_table_Pais
    
    @staticmethod
    def tablaCiudad():
        sql_create_table_Ciudad = """
        CREATE TABLE IF NOT EXISTS Ciudad (
            idCiudad INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            Pais_idPais INTEGER,
            FOREIGN KEY (Pais_idPais) REFERENCES Pais(idPais)
        );"""
        return sql_create_table_Ciudad
    
    @staticmethod
    def tablaDireccion():
        sql_create_table_Direccion = """
        CREATE TABLE IF NOT EXISTS Direccion (
        idDireccion INTEGER PRIMARY KEY AUTOINCREMENT,
        calle VARCHAR(45),
        numero VARCHAR(45),
        descripcion VARCHAR(45),
        Ciudad_idCiudad INTEGER,
        Ciudad_Pais_idPais INTEGER,
        FOREIGN KEY (Ciudad_idCiudad, Ciudad_Pais_idPais) REFERENCES Ciudad(idCiudad, Pais_idPais)
        );"""
        return sql_create_table_Direccion
    
    @staticmethod    
    def tablaRol():
        sql_create_table_Rol = """
        CREATE TABLE IF NOT EXISTS Rol (
            idRol INTEGER PRIMARY KEY AUTOINCREMENT,
            rol VARCHAR(45) UNIQUE
        );"""
        return sql_create_table_Rol
    
    @staticmethod    
    def tablaUsuario():
        sql_create_table_Usuario = """
        CREATE TABLE IF NOT EXISTS Usuario (
            idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            apellido VARCHAR(45),
            correo VARCHAR(45),
            telefono VARCHAR(45),
            fechaNacimiento DATE,
            imagenUsuario VARCHAR(250),
            Direccion_idDireccion INTEGER,
            Rol_idRol INTEGER,
            FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion),
            FOREIGN KEY (Rol_idRol) REFERENCES Rol(idRol)
        );"""
        return sql_create_table_Usuario
    
    @staticmethod
    def tablaEmpresa():
        sql_create_table_Empresa = """
        CREATE TABLE IF NOT EXISTS Empresa (
            idEmpresa INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            telefono VARCHAR(45),
            correo VARCHAR(45),
            cuil INTEGER,
            logoEmpresa VARCHAR(250),
            Direccion_idDireccion INTEGER,
            FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
        );"""
        return sql_create_table_Empresa
    
    @staticmethod
    def tablaAlmacenamiento():
        sql_create_table_Almacenamiento = """
        CREATE TABLE IF NOT EXISTS Almacenamiento (
            idAlmacenamiento INTEGER PRIMARY KEY AUTOINCREMENT,
            capacidadTotalM3 VARCHAR(45),
            usoM3 VARCHAR(45),
            Empresa_idEmpresa INTEGER,
            Direccion_idDireccion INTEGER,
            FOREIGN KEY (Empresa_idEmpresa) REFERENCES Empresa(idEmpresa),
            FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
        );"""
        return sql_create_table_Almacenamiento
    
    @staticmethod
    def tablaEnvio():
        sql_create_table_Envio = """
        CREATE TABLE IF NOT EXISTS Envio (
            idEnvio INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(45),
            estado VARCHAR(45),
            fechaDespacho DATE,
            fechaEntrega DATE,
            Direccion_idDireccion INTEGER,
            FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
        );"""
        return sql_create_table_Envio
    
    @staticmethod    
    def tablaFactura():
        sql_create_table_Factura = """
        CREATE TABLE IF NOT EXISTS Factura (
            idFactura INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(45),
            fechaEmision DATE,
            imagenFactura VARCHAR(250)
        );"""
        return sql_create_table_Factura
    
    @staticmethod
    def tablaPago():
        sql_create_table_Pago = """
        CREATE TABLE IF NOT EXISTS Pago (
            idPago INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(45),
            cuotas INTEGER,
            Factura_idFactura INTEGER,
            origen TEXT CHECK(origen IN ('Compra', 'Venta')),
            FOREIGN KEY (Factura_idFactura) REFERENCES Factura(idFactura)
        );"""
        return sql_create_table_Pago
    
    @staticmethod    
    def tablaVenta():
        sql_create_table_Venta = """
        CREATE TABLE IF NOT EXISTS Venta (
            idVenta INTEGER PRIMARY KEY AUTOINCREMENT,
            fechaVenta DATE,
            Usuario_idUsuario INTEGER,
            Envio_idEnvio INTEGER,
            Articulo_idArticulo INTEGER,
            Pago_idPago INTEGER,
            FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario),
            FOREIGN KEY (Envio_idEnvio) REFERENCES Envio(idEnvio),
            FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
            FOREIGN KEY (Pago_idPago) REFERENCES Pago(idPago)
        );"""
        return sql_create_table_Venta
    
    @staticmethod
    def tablaEditorial():
        sql_create_table_Editorial = """
        CREATE TABLE IF NOT EXISTS Editorial (
            idEditorial INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            imagenEditorial VARCHAR(250)
        );"""
        return sql_create_table_Editorial
    
    @staticmethod
    def tablaProveedor():
        sql_create_table_Proveedor = """
        CREATE TABLE IF NOT EXISTS Proveedor (
            idProveedor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            telefono VARCHAR(45),
            contactoPrincipal VARCHAR(45)
        );"""
        return sql_create_table_Proveedor
    
    @staticmethod
    def tablaDevolucion():
        sql_create_table_Devolucion = """
        CREATE TABLE IF NOT EXISTS Devolucion (
            idDevolucion INTEGER PRIMARY KEY AUTOINCREMENT,
            motivo VARCHAR(45),
            fechaDevolucion DATE,
            cantidad INTEGER,
            Pago_idPago INTEGER,
            FOREIGN KEY (Pago_idPago) REFERENCES Pago(idPago)
        );"""
        return sql_create_table_Devolucion
    
    @staticmethod
    def tablaGenero():
        sql_create_table_genero = """
        CREATE TABLE IF NOT EXISTS Genero (
            idGenero INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45)
        );"""
        return sql_create_table_genero
    
    @staticmethod
    def tablaLibro():
        sql_create_table_Libro = """
        CREATE TABLE IF NOT EXISTS Libro (
            idLibro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(45),
            idioma VARCHAR(45),
            tapa VARCHAR(45),
            anio INTEGER,
            isbn VARCHAR(45),
            paginas VARCHAR(45),
            edicion VARCHAR(45),
            edad_minima INTEGER,
            edad_maxima INTEGER,
            descripcion VARCHAR(45),
            imagen_tapa VARCHAR(250),
            Articulo_idArticulo INTEGER,
            Genero_idGenero INTEGER,
            Editorial_idEditorial INTEGER,
            FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
            FOREIGN KEY (Genero_idGenero) REFERENCES Genero(idGenero),
            FOREIGN KEY (Editorial_idEditorial) REFERENCES Editorial(idEditorial)
        );"""
        return sql_create_table_Libro
    
    @staticmethod
    def tablaAutor():
        sql_create_table_Autor = """
        CREATE TABLE IF NOT EXISTS Autor (
            idAutor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(45),
            apellido VARCHAR(45),
            imagenAutor VARCHAR(250)
        );"""
        return sql_create_table_Autor
    
    @staticmethod    
    def tablaCompra():
        sql_create_table_Compra = """
        CREATE TABLE IF NOT EXISTS Compra (
            idCompra INTEGER PRIMARY KEY AUTOINCREMENT,
            Almacenamiento_idAlmacenamiento INTEGER,
            Articulo_idArticulo INTEGER,
            fecha DATE,
            cantidad INTEGER,
            precioUnitario DOUBLE,
            Pago_idPago INTEGER,
            Proveedor_idProveedor INTEGER,
            FOREIGN KEY (Almacenamiento_idAlmacenamiento) REFERENCES Almacenamiento(idAlmacenamiento),
            FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
            FOREIGN KEY (Pago_idPago) REFERENCES Pago(idPago),
            FOREIGN KEY (Proveedor_idProveedor) REFERENCES Proveedor(idProveedor)
        );"""
        return sql_create_table_Compra
    
    @staticmethod    
    def tablaRevista():
        sql_create_table_Revista = """
        CREATE TABLE IF NOT EXISTS Revista (
            idRevista INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(45),
            numero INTEGER,
            anio INTEGER,
            mes INTEGER,
            dia INTEGER,
            Articulo_idArticulo INTEGER,
            Editorial_idEditorial INTEGER,
            Genero_idGenero INTEGER,
            FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
            FOREIGN KEY (Editorial_idEditorial) REFERENCES Editorial(idEditorial),
            FOREIGN KEY (Genero_idGenero) REFERENCES Genero(idGenero)
        );"""
        return sql_create_table_Revista
    
    @staticmethod    
    def tablaAutor_has_Libro():
        sql_create_table_Autor_has_Libro = """
        CREATE TABLE IF NOT EXISTS Autor_has_Libro (
            Autor_idAutor INTEGER,
            Libro_idLibro INTEGER,
            Libro_Articulo_idArticulo INTEGER,
            PRIMARY KEY (Autor_idAutor, Libro_idLibro, Libro_Articulo_idArticulo),
            FOREIGN KEY (Autor_idAutor) REFERENCES Autor(idAutor),
            FOREIGN KEY (Libro_idLibro, Libro_Articulo_idArticulo) REFERENCES Libro(idLibro, Articulo_idArticulo)
        );"""
        return sql_create_table_Autor_has_Libro
