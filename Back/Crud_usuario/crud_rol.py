from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox
import sys
import pymysql

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',  # Dirección del servidor MySQL
        user='root',       # Usuario de MySQL
        password='contraseña',  # Contraseña de MySQL
        database='BD_Libreria',  # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Funciones CRUD para la tabla Rol

# Crear un nuevo rol
def create_role(rol):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `BD_Libreria`.`Rol` (rol) VALUES (%s)"
            cursor.execute(sql, (rol,))
        connection.commit()
    finally:
        connection.close()

# Leer todos los roles
def read_roles():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Rol`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Actualizar un rol
def update_role(id_rol, rol):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `BD_Libreria`.`Rol` SET rol=%s WHERE idRol=%s"
            cursor.execute(sql, (rol, id_rol))
        connection.commit()
    finally:
        connection.close()

# Eliminar un rol
def delete_role(id_rol):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Rol` WHERE idRol=%s"
            cursor.execute(sql, (id_rol,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para la tabla Rol
class RoleCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Rol')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.rol_input = QLineEdit(self)
        self.rol_input.setPlaceholderText('Nombre del Rol')
        layout.addWidget(self.rol_input)

        self.create_button = QPushButton('Crear Rol', self)
        self.create_button.clicked.connect(self.create_role)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Rol', self)
        self.update_button.clicked.connect(self.update_role)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Rol', self)
        self.delete_button.clicked.connect(self.delete_role)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        roles = read_roles()
        self.table.setRowCount(len(roles))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID Rol', 'Rol'])
        for row_idx, role in enumerate(roles):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(role['idRol'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(role['rol']))

    def create_role(self):
        rol = self.rol_input.text()
        if rol:
            create_role(rol)
            self.load_data()
            self.rol_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'El campo del rol no puede estar vacío')

    def update_role(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un rol para actualizar')
            return

        id_rol = int(self.table.item(selected, 0).text())
        rol = self.rol_input.text()
        if rol:
            update_role(id_rol, rol)
            self.load_data()
            self.rol_input.clear()
        else:
            QMessageBox.warning(self, 'Error', 'El campo del rol no puede estar vacío')

    def delete_role(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un rol para eliminar')
            return

        id_rol = int(self.table.item(selected, 0).text())
        delete_role(id_rol)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    role_window = RoleCRUDApp()
    role_window.show()
    sys.exit(app.exec_())
