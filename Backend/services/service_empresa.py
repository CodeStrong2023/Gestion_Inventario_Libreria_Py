from Backend.controllers.controllers import Crud
from Backend.entities.entities import Empresa

class EmpresaService:
    def __init__(self, conn):
        self.conn = conn

    def crear_empresa(self, nombre, telefono, correo, cuil, logoEmpresa, Direccion_idDireccion):
        nueva_empresa = Empresa(
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            cuil=cuil,
            logoEmpresa=logoEmpresa,
            Direccion_idDireccion=Direccion_idDireccion
        )
        Crud.crear(nueva_empresa, self.conn)
        return nueva_empresa

    def buscar_empresa(self, idEmpresa):
        return Crud.leer(Empresa, self.conn, idEmpresa)

    def buscar_empresas(self):
        return Crud.leerTodos(Empresa, self.conn)

    def actualizar_empresa(self, idEmpresa, nombre, telefono, correo, cuil, logoEmpresa, Direccion_idDireccion):
        empresa = self.buscar_empresa(idEmpresa)
        if empresa:
            empresa.nombre = nombre
            empresa.telefono = telefono
            empresa.correo = correo
            empresa.cuil = cuil
            empresa.logoEmpresa = logoEmpresa
            empresa.Direccion_idDireccion = Direccion_idDireccion
            Crud.actualizar(empresa, self.conn)
            return empresa
        return None

    def eliminar_empresa(self, idEmpresa):
        Crud.eliminar(Empresa, self.conn, idEmpresa)

    def buscar_empresas_generico(self, criterio_busqueda):
        return Crud.buscar_generico(Empresa, self.conn, criterio_busqueda)

    