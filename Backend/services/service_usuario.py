from Backend.controllers.controllers import Crud
from Backend.entities.entities import Usuario, Direccion, Pais, Ciudad

class UsuarioService:
    def __init__(self, conn):
        self.conn = conn
    
    def crear_usuario(self, nombre="", apellido="",correo="", telefono="",fechaNacimiento="", Direccion_idDireccion=None,rol_idRol=None):
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            fechaNacimiento=fechaNacimiento,
            Direccion_idDireccion=Direccion_idDireccion,
            Rol_idRol=rol_idRol
        )
        Crud.crear(nuevo_usuario, self.conn)
        return nuevo_usuario
    
    def buscar_usuario(self, idUsuario):
        return Crud.leer(Usuario, self.conn, idUsuario)
    
    def buscar_usuarios(self):
        return Crud.leerTodos(Usuario, self.conn)
    
    def eliminar_usuario(self, idUsuario):

        Crud.eliminar(Usuario, self.conn, idUsuario)
    
    def actualizar_usuario(self, idUsuario, nombre="", apellido="",correo="", telefono="",fechaNacimiento="", Direccion_idDireccion=None,rol_idRol=None):
        usuario = self.buscar_usuario(idUsuario)
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.correo = correo
        usuario.telefono = telefono
        usuario.fechaNacimiento = fechaNacimiento
        usuario.Direccion_idDireccion = Direccion_idDireccion
        usuario.rol_idRol = rol_idRol
        Crud.actualizar(usuario, self.conn)
        return usuario

    def buscar_usuarios_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Usuario, self.conn, criterio_busqueda)
