from Backend.controllers.controllers import Crud
from Backend.entities.entities import Direccion, Pais, Ciudad

class DireccionService:
    def __init__(self, conn):
        self.conn = conn
    
    def crear_direccion(self, calle="", numero="", descripcion="", Ciudad_idCiudad=None, Ciudad_Pais_idPais=None):
        nueva_direccion = Direccion(
            calle=calle,
            numero=numero,
            descripcion=descripcion,
            Ciudad_idCiudad=Ciudad_idCiudad,
            Ciudad_Pais_idPais=Ciudad_Pais_idPais
        )
        Crud.crear(nueva_direccion, self.conn)
        return nueva_direccion
    

    def buscar_direccion(self, idDireccion):
        return Crud.leer(Direccion, self.conn, idDireccion)
    
    def buscar_ciudad(self, idCiudad):
        return Crud.leer(Ciudad, self.conn, idCiudad)
    
    def crear_ciudad(self, nombre, idPais):
        nueva_ciudad = Ciudad(nombre=nombre, Pais_idPais=idPais)
        Crud.crear(nueva_ciudad, self.conn)
        return nueva_ciudad.idCiudad
    
    def buscar_pais(self, idPais):
        return Crud.leer(Pais, self.conn, idPais)
    
    def eliminar_direccion(self, idDireccion):
        Crud.eliminar(Direccion, self.conn, idDireccion)
        
    def crear_pais(self, nombre):
        nuevo_pais = Pais(nombre=nombre)
        Crud.crear(nuevo_pais, self.conn)
        return nuevo_pais.idPais
        
    def pais_existe(self, nombre_pais):
        paises = Crud.leerTodos(Pais, self.conn)
        idCountry =self.obtener_id_country(nombre_pais, paises)
        if idCountry:
            return idCountry
        else:
            idCountry = self.crear_pais(nombre_pais)
            return idCountry

    def obtener_id_country(self, nombre_pais, lista_paises):
        for country in lista_paises:
            if country['nombre'] == nombre_pais:
                return country['idPais']
        return False
    
    def ciudad_existe(self, nombre_ciudad, idPais):
        ciudades = Crud.leerTodos(Ciudad, self.conn)
        idCity = self.obtener_id_ciudad(nombre_ciudad, ciudades)
        if idCity:
            return idCity
        else:
            idCity = self.crear_ciudad(nombre_ciudad, idPais)
            return idCity
        
    def obtener_id_ciudad(self, nombre_ciudad, lista_ciudades):
        for city in lista_ciudades:
            if city['nombre'] == nombre_ciudad:
                return city['idCiudad']
        return False
    
    def buscar_direcciones_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Direccion, self.conn, criterio_busqueda)

    def actualizar_direccion(self, idDireccion, calle, numero, descripcion, Ciudad_idCiudad, Ciudad_Pais_idPais):
        direccion = self.buscar_direccion(idDireccion)
        nueva_direccion = Direccion(
            idDireccion = idDireccion,
            calle = calle,
            numero = numero,
            descripcion = descripcion,
            Ciudad_idCiudad = Ciudad_idCiudad,
            Ciudad_Pais_idPais = Ciudad_Pais_idPais
        )
        if direccion:
            Crud.actualizar(Direccion, self.conn, nueva_direccion)
        return nueva_direccion
        
    def leer_todos_paises(self):
        #devolverlos en formato []
        paises =Crud.leerTodos(Pais, self.conn)
        #pasar resultado a formato de lista
        nombres_paises = [pais['nombre'] for pais in paises]  
        
        return nombres_paises
    
    #funcion para leer todas las ciudades segun el id de pais vinculado
    def leer_todas_ciudades_pais(self, idPais):
        ciudades = Crud.leerTodos(Ciudad, self.conn)
        ciudades_pais = [ciudad['nombre'] for ciudad in ciudades if ciudad['Pais_idPais'] == idPais]
        
        return ciudades_pais
    
    def leer_todas_ciudades(self):
        ciudades = Crud.leerTodos(Ciudad, self.conn)
        nombres_ciudades = [ciudad['nombre'] for ciudad in ciudades]
        return nombres_ciudades