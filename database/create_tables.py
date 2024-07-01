
class CreateTables():
        
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
                idCiudad INTEGER,
                nombre VARCHAR(45),
                Pais_idPais INTEGER,
                PRIMARY KEY (idCiudad, Pais_idPais),
                FOREIGN KEY (Pais_idPais) REFERENCES Pais(idPais)
            );"""
            return sql_create_table_Ciudad
        
        @staticmethod
        def tablaDireccion():            
            sql_create_table_Direccion = """
            CREATE TABLE IF NOT EXISTS Direccion (
                idDireccion INTEGER,
                calle VARCHAR(45),
                numero VARCHAR(45),
                descripcion VARCHAR(45),
                Ciudad_idCiudad INTEGER,
                Ciudad_Pais_idPais INTEGER,
                PRIMARY KEY (idDireccion, Ciudad_idCiudad, Ciudad_Pais_idPais),
                FOREIGN KEY (Ciudad_idCiudad, Ciudad_Pais_idPais) REFERENCES Ciudad(idCiudad, Pais_idPais)
            );"""
            return sql_create_table_Direccion
        
        @staticmethod    
        def tablaRol():
            sql_create_table_Rol = """
            CREATE TABLE IF NOT EXISTS Rol (
                idRol INTEGER PRIMARY KEY AUTOINCREMENT,
                rol VARCHAR(45)
            );"""
            return sql_create_table_Rol
        
        @staticmethod    
        def tablaUsuario():
            sql_create_table_Usuario = """
            CREATE TABLE IF NOT EXISTS Usuario (
                idUsuario INTEGER,
                nombre VARCHAR(45),
                apellido VARCHAR(45),
                correo VARCHAR(45),
                telefono VARCHAR(45),
                fechaNacimiento DATE,
                imagenUsuario VARCHAR(250),
                Direccion_idDireccion INTEGER,
                Rol_idRol INTEGER,
                PRIMARY KEY (idUsuario, Direccion_idDireccion, Rol_idRol),
                FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion),
                FOREIGN KEY (Rol_idRol) REFERENCES Rol(idRol)
            );"""
            return sql_create_table_Usuario
        
        @staticmethod
        def tablaEmpresa():    
            sql_create_table_Empresa = """
            CREATE TABLE IF NOT EXISTS Empresa (
                idEmpresa INTEGER,
                nombre VARCHAR(45),
                telefono VARCHAR(45),
                correo VARCHAR(45),
                cuil INTEGER,
                logoEmpresa VARCHAR(250),
                Direccion_idDireccion INTEGER,
                PRIMARY KEY (idEmpresa, Direccion_idDireccion),
                FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
            );"""
            return sql_create_table_Empresa
        
        @staticmethod
        def tablaAlmacenamiento():    
            sql_create_table_Almacenamiento = """
            CREATE TABLE IF NOT EXISTS Almacenamiento (
                idAlmacenamiento INTEGER,
                capacidadTotalM3 VARCHAR(45),
                usoM3 VARCHAR(45),
                Empresa_idEmpresa INTEGER,
                Direccion_idDireccion INTEGER,
                PRIMARY KEY (idAlmacenamiento, Empresa_idEmpresa, Direccion_idDireccion),
                FOREIGN KEY (Empresa_idEmpresa) REFERENCES Empresa(idEmpresa),
                FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
            );"""
            return sql_create_table_Almacenamiento
        
        @staticmethod
        def tablaEnvio():    
            sql_create_table_Envio = """
            CREATE TABLE IF NOT EXISTS Envio (
                idEnvio INTEGER,
                tipo VARCHAR(45),
                estado VARCHAR(45),
                fechaDespacho DATE,
                fechaEntrega DATE,
                Direccion_idDireccion INTEGER,
                PRIMARY KEY (idEnvio, Direccion_idDireccion),
                FOREIGN KEY (Direccion_idDireccion) REFERENCES Direccion(idDireccion)
            );"""
            return sql_create_table_Envio
        
        @staticmethod    
        def tablaFacturas():    
            sql_create_table_Facturas = """
            CREATE TABLE IF NOT EXISTS Facturas (
                idFacturas INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo VARCHAR(45),
                fechaEmision DATE,
                imagenFactura VARCHAR(250)
            );"""
            return sql_create_table_Facturas
        
        @staticmethod
        def tablaPago():
            sql_create_table_Pago = """
            CREATE TABLE IF NOT EXISTS Pago (
                idPago INTEGER,
                tipo VARCHAR(45),
                cuotas INTEGER,
                Facturas_idFacturas INTEGER,
                origen TEXT CHECK(origen IN ('Compra', 'Venta')),
                PRIMARY KEY (idPago, Facturas_idFacturas),
                FOREIGN KEY (Facturas_idFacturas) REFERENCES Facturas(idFacturas)
            );"""
            return sql_create_table_Pago
        
        @staticmethod    
        def tablaVenta():    
            sql_create_table_Venta = """
            CREATE TABLE IF NOT EXISTS Venta (
                idVenta INTEGER,
                fechaVenta DATE,
                Usuario_idUsuario INTEGER,
                Envio_idEnvio INTEGER,
                Articulo_idArticulo INTEGER,
                Pago_idPago INTEGER,
                PRIMARY KEY (idVenta, Usuario_idUsuario, Envio_idEnvio, Articulo_idArticulo, Pago_idPago),
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
                idDevolucion INTEGER,
                motivo VARCHAR(45),
                fechaDevolucion DATE,
                cantidad INTEGER,
                Pago_idPago INTEGER,
                PRIMARY KEY (idDevolucion, Pago_idPago),
                FOREIGN KEY (Pago_idPago) REFERENCES Pago(idPago)
            );"""
            return sql_create_table_Devolucion
        
        @staticmethod
        def tablaGenero():    
            sql_create_table_genero = """
            CREATE TABLE IF NOT EXISTS genero (
                idgenero INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(45)
            );"""
            return sql_create_table_genero
        
        @staticmethod
        def tablaLibro():    
            sql_create_table_Libro = """
            CREATE TABLE IF NOT EXISTS Libro (
                idLibro INTEGER,
                titulo VARCHAR(45),
                idioma VARCHAR(45),
                tapa VARCHAR(45),
                año INTEGER,
                isbn VARCHAR(45),
                paginas VARCHAR(45),
                edicion VARCHAR(45),
                edad_minima INTEGER,
                edad_maxima INTEGER,
                descripcion VARCHAR(45),
                imagen_tapa VARCHAR(250),
                Articulo_idArticulo INTEGER,
                genero_idgenero INTEGER,
                Editorial_idEditorial INTEGER,
                PRIMARY KEY (idLibro, Articulo_idArticulo, genero_idgenero, Editorial_idEditorial),
                UNIQUE (Articulo_idArticulo),
                FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
                FOREIGN KEY (genero_idgenero) REFERENCES genero(idgenero),
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
                CompraId INTEGER,
                Almacenamiento_idAlmacenamiento INTEGER,
                Articulo_idArticulo INTEGER,
                fecha DATE,
                cantidad INTEGER,
                precioUnitario DOUBLE,
                Pago_idPago INTEGER,
                Proveedor_idProveedor INTEGER,
                PRIMARY KEY (CompraId, Almacenamiento_idAlmacenamiento, Articulo_idArticulo, Pago_idPago, Proveedor_idProveedor),
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
                idRevista INTEGER,
                titulo VARCHAR(45),
                numero INTEGER,
                anio INTEGER,
                mes INTEGER,
                dia INTEGER,
                Articulo_idArticulo INTEGER,
                Editorial_idEditorial INTEGER,
                genero_idgenero INTEGER,
                PRIMARY KEY (idRevista, Articulo_idArticulo, Editorial_idEditorial, genero_idgenero),
                UNIQUE (Articulo_idArticulo),
                FOREIGN KEY (Articulo_idArticulo) REFERENCES Articulo(idArticulo),
                FOREIGN KEY (Editorial_idEditorial) REFERENCES Editorial(idEditorial),
                FOREIGN KEY (genero_idgenero) REFERENCES genero(idgenero)
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