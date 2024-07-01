import sqlite3
from Backend.database.create_tables import CreateTables
from Backend.database.insert_initial_data import CreateInitialData

class Connection:
    
    def __init__(self):
        try:
            self.conn = sqlite3.connect('./Backend/database/BD_Libreria.db')
            self.createTables()
            self.insertInitialData()
        except Exception as e:
            print(e)
            
    def abrirConexion(self):
        return self.conn
    
    def cerrarConexion(self):
        self.conn.close()

    def createTables(self):        
        # Create all tables
        cursor = self.conn.cursor()
        cursor.execute(CreateTables.tablaArticulo())
        cursor.execute(CreateTables.tablaPais())
        cursor.execute(CreateTables.tablaCiudad())
        cursor.execute(CreateTables.tablaDireccion())
        cursor.execute(CreateTables.tablaRol())
        cursor.execute(CreateTables.tablaUsuario())
        cursor.execute(CreateTables.tablaEmpresa())
        cursor.execute(CreateTables.tablaAlmacenamiento())
        cursor.execute(CreateTables.tablaEnvio())
        cursor.execute(CreateTables.tablaFactura())
        cursor.execute(CreateTables.tablaPago())
        cursor.execute(CreateTables.tablaVenta())
        cursor.execute(CreateTables.tablaEditorial())
        cursor.execute(CreateTables.tablaProveedor())
        cursor.execute(CreateTables.tablaDevolucion())
        cursor.execute(CreateTables.tablaGenero())
        cursor.execute(CreateTables.tablaLibro())
        cursor.execute(CreateTables.tablaAutor())
        cursor.execute(CreateTables.tablaCompra())
        cursor.execute(CreateTables.tablaRevista())
        cursor.execute(CreateTables.tablaAutor_has_Libro())
        self.conn.commit()
        cursor.close()
        
        print("Tables created successfully")
    
    def insertInitialData(self):
        # Insert initial data
        cursor = self.conn.cursor()
        
        #evaluar si existen datos en la base de datos antes de insertar
        cursor.execute("SELECT * FROM Pais")
        rows = cursor.fetchall()
        if len(rows) > 0:
            print("Initial data already inserted")
            return
        else:
            cursor.execute(CreateInitialData.crearRol())
            cursor.execute(CreateInitialData.crearRolCliente()) 
        print("Inserting initial data")
        
        
        
        cursor.execute(CreateInitialData.crearPaises())
        cursor.execute(CreateInitialData.crearCiudades())
        cursor.execute(CreateInitialData.crearDirecciones())
        cursor.execute(CreateInitialData.crearEmpresa())
        cursor.execute(CreateInitialData.crearAlmacenamiento())

        cursor.execute(CreateInitialData.crearUsuario())
        cursor.execute(CreateInitialData.crearEditoriales())
        cursor.execute(CreateInitialData.crearGeneros())
        cursor.execute(CreateInitialData.crearArticulos())
        cursor.execute(CreateInitialData.crearLibros())
        cursor.execute(CreateInitialData.crearRevistas())
        cursor.execute(CreateInitialData.crearProveedor())
        cursor.execute(CreateInitialData.crearFactura())
        cursor.execute(CreateInitialData.crearPago())
        cursor.execute(CreateInitialData.asociarLibros())
        cursor.execute(CreateInitialData.asociarRevistas())
        cursor.execute(CreateInitialData.crearVenta())
        cursor.execute(CreateInitialData.crearAutor())

        cursor.execute(CreateInitialData.crearEnvio())
        cursor.execute(CreateInitialData.crearCompra())
        cursor.execute(CreateInitialData.crearDevolucion())
        
        self.conn.commit()
        cursor.close()
        
        print("Initial data inserted successfully")
        
