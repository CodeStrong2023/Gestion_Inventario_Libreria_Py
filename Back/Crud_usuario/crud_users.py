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

# Funciones CRUD
# Crear un nuevo usuario
def create_user(nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO `BD_Libreria`.`Usuario` (nombre, apellido, correo, telefono, fechaNacimiento, imagenUsuario, Direccion_idDireccion, Rol_idRol)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id))
        connection.commit()
    finally:
        connection.close()

# Leer usuarios
def read_users():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Usuario`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Actualizar un usuario
def update_user(id_usuario, nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Usuario SET nombre=%s, apellido=%s, correo=%s, telefono=%s, fechaNacimiento=%s, imagenUsuario=%s, Direccion_idDireccion=%s, Rol_idRol=%s
            WHERE idUsuario=%s
            """
            cursor.execute(sql, (nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id, id_usuario))
        connection.commit()
    finally:
        connection.close()

# Eliminar un usuario
def delete_user(id_usuario):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Usuario WHERE idUsuario=%s"
            cursor.execute(sql, (id_usuario,))
        connection.commit()
    finally:
        connection.close()

# Aplicacion PyQt5
class CRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Usuario')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')
        layout.addWidget(self.nombre_input)

        self.apellido_input = QLineEdit(self)
        self.apellido_input.setPlaceholderText('Apellido')
        layout.addWidget(self.apellido_input)

        self.correo_input = QLineEdit(self)
        self.correo_input.setPlaceholderText('Correo')
        layout.addWidget(self.correo_input)

        self.telefono_input = QLineEdit(self)
        self.telefono_input.setPlaceholderText('Teléfono')
        layout.addWidget(self.telefono_input)

        self.fecha_nacimiento_input = QLineEdit(self)
        self.fecha_nacimiento_input.setPlaceholderText('Fecha de Nacimiento (YYYY-MM-DD)')
        layout.addWidget(self.fecha_nacimiento_input)

        self.imagen_usuario_input = QLineEdit(self)
        self.imagen_usuario_input.setPlaceholderText('Imagen Usuario')
        layout.addWidget(self.imagen_usuario_input)

        self.direccion_id_input = QLineEdit(self)
        self.direccion_id_input.setPlaceholderText('ID Dirección')
        layout.addWidget(self.direccion_id_input)

        self.rol_id_input = QLineEdit(self)
        self.rol_id_input.setPlaceholderText('ID Rol')
        layout.addWidget(self.rol_id_input)

        self.create_button = QPushButton('Crear Usuario', self)
        self.create_button.clicked.connect(self.create_user)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Usuario', self)
        self.update_button.clicked.connect(self.update_user)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Usuario', self)
        self.delete_button.clicked.connect(self.delete_user)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        users = read_users()
        self.table.setRowCount(len(users))
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido', 'Correo', 'Teléfono', 'Fecha de Nacimiento', 'Imagen', 'ID Dirección', 'ID Rol'])
        for row_idx, user in enumerate(users):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user['idUsuario'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(user['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(user['apellido']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(user['correo']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(user['telefono']))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(user['fechaNacimiento'])))
            self.table.setItem(row_idx, 6, QTableWidgetItem(user['imagenUsuario']))
            self.table.setItem(row_idx, 7, QTableWidgetItem(str(user['Direccion_idDireccion'])))
            self.table.setItem(row_idx, 8, QTableWidgetItem(str(user['Rol_idRol'])))

    def create_user(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        correo = self.correo_input.text()
        telefono = self.telefono_input.text()
        fecha_nacimiento = self.fecha_nacimiento_input.text()
        imagen_usuario = self.imagen_usuario_input.text()
        direccion_id = int(self.direccion_id_input.text())
        rol_id = int(self.rol_id_input.text())

        create_user(nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id)
        self.load_data()

    def update_user(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un usuario para actualizar')
            return

        id_usuario = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        correo = self.correo_input.text()
        telefono = self.telefono_input.text()
        fecha_nacimiento = self.fecha_nacimiento_input.text()
        imagen_usuario = self.imagen_usuario_input.text()
        direccion_id = int(self.direccion_id_input.text())
        rol_id = int(self.rol_id_input.text())

        update_user(id_usuario, nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id)
        self.load_data()

    def delete_user(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un usuario para eliminar')
            return

        id_usuario = int(self.table.item(selected, 0).text())
        delete_user(id_usuario)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CRUDApp()
    window.show()
    sys.exit(app.exec_())
