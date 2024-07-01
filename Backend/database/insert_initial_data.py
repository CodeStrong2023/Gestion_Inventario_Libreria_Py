
class CreateInitialData:
    
    @staticmethod
    def crearPaises():
        sql_insert_Pais = """
        INSERT OR IGNORE INTO Pais (`idPais`, `nombre`) VALUES
        (1, 'Argentina'),
        (2, 'Bolivia'),
        (3, 'Brazil'),
        (4, 'Chile'),
        (5, 'Colombia'),
        (6, 'Costa Rica'),
        (7, 'Cuba'),
        (8, 'Ecuador'),
        (9, 'El Salvador'),
        (10, 'Guatemala');
        """
       
        return sql_insert_Pais
    
    @staticmethod
    def crearCiudades():
        sql_insert_Ciudad = """
        INSERT OR IGNORE INTO Ciudad (`idCiudad`, `nombre`, `Pais_idPais`) VALUES
        -- Argentina
        (1, 'Buenos Aires', 1),
        (2, 'Córdoba', 1),
        (3, 'Rosario', 1),
        -- Bolivia
        (4, 'La Paz', 2),
        (5, 'Santa Cruz de la Sierra', 2),
        (6, 'Cochabamba', 2),
        -- Brasil
        (7, 'São Paulo', 3),
        (8, 'Río de Janeiro', 3),
        (9, 'Brasilia', 3),
        -- Chile
        (10, 'Santiago', 4),
        (11, 'Valparaíso', 4),
        (12, 'Concepción', 4),
        -- Colombia
        (13, 'Bogotá', 5),
        (14, 'Medellín', 5),
        (15, 'Cali', 5),
        -- Costa Rica
        (16, 'San José', 6),
        (17, 'Alajuela', 6),
        (18, 'Cartago', 6),
        -- Cuba
        (19, 'La Habana', 7),
        (20, 'Santiago de Cuba', 7),
        (21, 'Camagüey', 7),
        -- Ecuador
        (22, 'Quito', 8),
        (23, 'Guayaquil', 8),
        (24, 'Cuenca', 8),
        -- El Salvador
        (25, 'San Salvador', 9),
        (26, 'Santa Ana', 9),
        (27, 'San Miguel', 9),
        -- Guatemala
        (28, 'Ciudad de Guatemala', 10),
        (29, 'Mixco', 10),
        (30, 'Quetzaltenango', 10),
        -- Honduras
        (31, 'Tegucigalpa', 11),
        (32, 'San Pedro Sula', 11),
        (33, 'Choloma', 11),
        -- México
        (34, 'Ciudad de México', 12),
        (35, 'Guadalajara', 12),
        (36, 'Monterrey', 12),
        -- Nicaragua
        (37, 'Managua', 13),
        (38, 'León', 13),
        (39, 'Masaya', 13),
        -- Panamá
        (40, 'Ciudad de Panamá', 14),
        (41, 'Colón', 14),
        (42, 'David', 14),
        -- Paraguay
        (43, 'Asunción', 15),
        (44, 'Ciudad del Este', 15),
        (45, 'San Lorenzo', 15),
        -- Perú
        (46, 'Lima', 16),
        (47, 'Arequipa', 16),
        (48, 'Trujillo', 16),
        -- República Dominicana
        (49, 'Santo Domingo', 17),
        (50, 'Santiago de los Caballeros', 17),
        (51, 'La Romana', 17),
        -- Uruguay
        (52, 'Montevideo', 18),
        (53, 'Salto', 18),
        (54, 'Paysandú', 18),
        -- Venezuela
        (55, 'Caracas', 19),
        (56, 'Maracaibo', 19),
        (57, 'Valencia', 19);
        """
        
        return sql_insert_Ciudad
    
    @staticmethod
    def crearDirecciones():
        sql_insert_Direccion = """
        INSERT OR IGNORE INTO Direccion ( `calle`, `numero`, `descripcion`, `Ciudad_idCiudad`, `Ciudad_Pais_idPais`)
        VALUES ( 'Calle Ejemplo', '123', 'Descripción Ejemplo', 1, 1),
               ( 'Calle Ejemplo2', '123', 'Descripción Ejemplo', 1, 1);
        """
        
        return sql_insert_Direccion

    @staticmethod
    def crearEmpresa():
        sql_insert_Empresa = """
        INSERT INTO Empresa ( `nombre`, `telefono`, `correo`, `cuil`, `logoEmpresa`, `Direccion_idDireccion`)
        VALUES ( 'Libros Ficticios SA', '123456789', 'contacto@librosficticios.com', 12, 'logo.png', 1);
        """
       
        return sql_insert_Empresa
    
    @staticmethod
    def crearAlmacenamiento():
        sql_insert_Almacenamiento = """
        INSERT INTO Almacenamiento ( `capacidadTotalM3`, `usoM3`, `Empresa_idEmpresa`, `Direccion_idDireccion`)
        VALUES ( '5000', '2000', 1, 1);
        """
        
        return sql_insert_Almacenamiento

    @staticmethod
    def crearEditoriales():
        sql_insert_Editorial = """
        INSERT OR IGNORE INTO Editorial ( `nombre`, `imagenEditorial`)
        VALUES 
        ( 'Editorial Ejemplo', 'https://www.escuelacmyk.com/wp-content/uploads/2021/05/blog-cmyk-2021_que-es-ilustracion-editorial.png'),
        ( 'Editorial Ejemplo2', 'https://www.escuelacmyk.com/wp-content/uploads/2021/05/blog-cmyk-2021_que-es-ilustracion-editorial.png'),
        ( 'Editorial Ejemplo3', 'https://www.escuelacmyk.com/wp-content/uploads/2021/05/blog-cmyk-2021_que-es-ilustracion-editorial.png'),
        ( 'Editorial Ejemplo4', 'https://www.escuelacmyk.com/wp-content/uploads/2021/05/blog-cmyk-2021_que-es-ilustracion-editorial.png');
        """
        
        return sql_insert_Editorial

    @staticmethod
    def crearGeneros():
        sql_insert_Genero = """
        INSERT INTO Genero (nombre) VALUES 
        ('Ficción'), ('Terror'), ('Infantil'), ('Aventura'), ('Deporte');
        """
      
        return sql_insert_Genero

    @staticmethod
    def crearArticulos():
        sql_insert_Articulo = """
        INSERT INTO Articulo ( `alto`, `ancho`, `peso`, `precio`, `tipo` )
        VALUES
        ( '20', '15', '0.5', 20.00,"Libro"),
        ( '20', '15', '0.5',  22.00, "Libro"),
        ( '20', '15', '0.5',  5.00,"Revista"),
        ( '20', '15', '0.5',  5.00,"Revista"),
        ( '20', '15', '0.5',  22.00, "Libro"),
        ( '20', '15', '0.5',  22.00, "Libro"),
        ( '20', '15', '0.5',  22.00, "Libro"),
        ( '20', '15', '0.5',  5.00,"Revista"),
        ( '20', '15', '0.5',  5.00,"Revista"),
        ( '20', '15', '0.5',  6.00, "Revista");
        """
     
        return sql_insert_Articulo

    @staticmethod
    def crearLibros():
        sql_insert_Libro = """
        INSERT OR IGNORE INTO Libro ( `titulo`, `idioma`, `tapa`, `anio`, `isbn`, `paginas`, `edicion`, `edad_minima`, `edad_maxima`, `descripcion`, `imagen_tapa`, `Articulo_idArticulo`, `Genero_idGenero`, `Editorial_idEditorial`)
        VALUES
        ( 'Libro 1', 'Español', 'Dura', 2023, '1234567890123', '300', '1ra', 12, 99, 'Descripción del Libro 1', 'tapa1.png', 1, 1, 1),
        ( 'Libro 2', 'Español', 'Blanda', 2023, '1234567890124', '350', '1ra', 12, 99, 'Descripción del Libro 2', 'tapa2.png', 2, 1, 1),
        ( 'Nombre del Libro1', 'Español', 'Dura', 2023, '978-3-16-148413-0', '300', 'Primera', 8, 14, 'Descripción del libro', 'imagen_tapa.jpg', 5, 1, 1),
        ( 'Nombre del Libro2', 'Español', 'Dura', 2023, '978-3-16-148413-0', '300', 'Primera', 8, 14, 'Descripción del libro', 'imagen_tapa.jpg', 6, 1, 1),
        ( 'Nombre del Libro3', 'Español', 'Dura', 2023, '978-3-16-148413-0', '300', 'Primera', 8, 14, 'Descripción del libro', 'imagen_tapa.jpg', 7, 1, 1);
        """
        
        return sql_insert_Libro

    @staticmethod
    def crearRevistas():
        sql_insert_Revista = """
        INSERT OR IGNORE INTO Revista ( `titulo`, `numero`, `anio`, `mes`, `dia`, `Articulo_idArticulo`, `Editorial_idEditorial`, `Genero_idGenero`)
        VALUES
        ( 'Revista 1', 1, 2023, 6, 1, 3, 1, 1),
        ( 'Revista 2', 2, 2023, 7, 1, 4, 1, 1),
        ( 'Nombre de la Revista1', 5, 2024, 6, 1, 8, 2, 2),
        ( 'Nombre de la Revista2', 5, 2024, 6, 1, 9, 2, 2),
        ( 'Nombre de la Revista3', 5, 2024, 6, 1, 10, 2, 2);
        """
      
        return sql_insert_Revista

    @staticmethod
    def crearProveedor():
        sql_insert_Proveedor = """
        INSERT INTO Proveedor (nombre, telefono, contactoPrincipal) VALUES 
        ('Proveedor 1', '123456789', 'Contacto 1'),
        ('Proveedor 2', '987654321', 'Contacto 2'),
        ('Proveedor 3', '111222333', 'Contacto 3'),
        ('Proveedor 4', '444555666', 'Contacto 4'),
        ('Proveedor 5', '777888999', 'Contacto 5');
        """
     
        return sql_insert_Proveedor

    @staticmethod
    def crearFactura():
        sql_insert_Factura = """
        INSERT INTO Factura (tipo, fechaEmision) VALUES 
        ('Compra', '2024-06-02'),
        ('Compra', '2024-06-02'),
        ('Compra', '2024-06-02');
        """
        
        return sql_insert_Factura

    @staticmethod
    def crearPago():
        sql_insert_Pago = """
        INSERT INTO Pago (tipo, cuotas, Factura_idFactura) VALUES 
        ('Efectivo', 1,1),
        ('Tarjeta', 3,2),
        ('Transferencia', 1,3);
        """
       
        return sql_insert_Pago

    @staticmethod
    def asociarLibros():
        sql_insert_CompraLibros = """
        INSERT INTO Compra (Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario, Pago_idPago, Proveedor_idProveedor)
        SELECT 1, idLibro, '2024-06-02', 10, precio, 1, 1 FROM Libro L
        JOIN Articulo A ON L.Articulo_idArticulo = A.idArticulo
        WHERE idLibro BETWEEN 1 AND 11;
        """
     
        return sql_insert_CompraLibros

    @staticmethod
    def asociarRevistas():
        sql_insert_CompraRevistas = """
        INSERT INTO Compra (Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario, Pago_idPago, Proveedor_idProveedor)
        SELECT 1, idRevista, '2024-06-02', 10, precio, 2, 2 FROM Revista R
        JOIN Articulo A ON R.Articulo_idArticulo = A.idArticulo
        WHERE idRevista BETWEEN 1 AND 11;
        """
       
        return sql_insert_CompraRevistas
    
    @staticmethod
    def crearVenta():
        sql_insert_Venta = """
        INSERT INTO Venta (fechaVenta, Usuario_idUsuario, Envio_idEnvio, Articulo_idArticulo, Pago_idPago)
        VALUES ('2024-06-02', 4, 1, 1, 1);
        """
    
        return sql_insert_Venta
    
    @staticmethod
    def crearRol():
            sql_insert_Rol = """
            INSERT INTO Rol VALUES (null, 'Administrador');"""
        
            return sql_insert_Rol
    def crearRolCliente():
        sql_insert_Rol = """
        INSERT INTO Rol VALUES (null, 'Cliente');"""
    
        return sql_insert_Rol
    @staticmethod 
    def crearUsuario():
            sql_insert_Usuario = """
            INSERT INTO Usuario (idUsuario, nombre, apellido, correo, telefono, fechaNacimiento, imagenUsuario, Direccion_idDireccion, Rol_idRol)
            VALUES (
                null,           -- idUsuario
                'Admin',    -- nombre del usuario
                'Admin',  -- apellido del usuario
                'usuario@example.com',  -- correo del usuario
                '123456789',      -- teléfono del usuario
                '1990-01-01',     -- fecha de nacimiento del usuario (formato 'YYYY-MM-DD')
                'imagen.jpg',     -- imagen del usuario
                1,                -- id de la dirección del usuario (debe existir en la tabla Direccion)
                1                 -- id del rol del usuario (debe existir en la tabla Rol)
            );
            """
          
            return sql_insert_Usuario
    @staticmethod
    def crearUsuarioCliente():
        sql_insert_Usuario = """
        INSERT INTO Usuario (idUsuario, nombre, apellido, correo, telefono, fechaNacimiento, imagenUsuario, Direccion_idDireccion, Rol_idRol)
        VALUES (
            null,                   -- idUsuario (se genera automáticamente)
            'Cliente',              -- nombre del usuario
            'Nuevo',                -- apellido del usuario
            'cliente@example.com',  -- correo del usuario
            '987654321',            -- teléfono del usuario
            '1995-01-01',           -- fecha de nacimiento del usuario (formato 'YYYY-MM-DD')
            'cliente.jpg',          -- imagen del usuario
            1,                      -- id de la dirección del usuario (debe existir en la tabla Direccion)
            2                       -- id del rol del usuario (debe existir en la tabla Rol, asumiendo que el id 2 es para clientes)
        );
        """
        
        return sql_insert_Usuario
    
    @staticmethod
    def crearEnvio():
        sql_insert_Envio = """
        INSERT INTO Envio (tipo, estado, fechaDespacho, fechaEntrega, Direccion_idDireccion)
        VALUES ('Normal', 'En camino', '2024-06-02', '2024-06-05', 1);
        """
        
        return sql_insert_Envio
    
    @staticmethod
    def crearAutor():
        sql_insert_Autor = """
        INSERT INTO Autor (nombre, apellido, imagenAutor)
        VALUES ('Jose', 'Perez', 'imagen.jpg');
        """
        
        return sql_insert_Autor
    
    @staticmethod
    def crearDevolucion():
        sql_insert_Devolucion = """
        INSERT INTO Devolucion (motivo,fechaDevolucion, cantidad, Pago_idPago)
        VALUES ('Producto dañado', '2024-06-02', 1, 1);
        """
        
        return sql_insert_Devolucion
    
    @staticmethod
    def crearCompra():
        sql_insert_Compra = """
        INSERT INTO Compra ( Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario, Pago_idPago, Proveedor_idProveedor)
        VALUES (1, 1, '2024-06-02', 10, 20.00, 1, 1);
        """
        
        return sql_insert_Compra