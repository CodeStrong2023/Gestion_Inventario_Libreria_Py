from database.connection import Connection
from database.PruebaCrud import PruebaCrud

def main():

    conn = Connection().abrirConexion()
    PruebaCrud.pruebaCrear(conn)
    PruebaCrud.pruebaLeer(conn)
    PruebaCrud.pruebaActualizar(conn)
    PruebaCrud.pruebaEliminar(conn)
    PruebaCrud.pruebaLeerTodos(conn)
    


if __name__ == "__main__":
    main()
