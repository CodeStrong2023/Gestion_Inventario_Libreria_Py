from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QComboBox, QDateEdit
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

# Funciones CRUD para la tabla Usuario

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

# Leer todos los usuarios
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
            UPDATE `BD_Libreria`.`Usuario`
            SET nombre=%s, apellido=%s, correo=%s, telefono=%s, fechaNacimiento=%s, imagenUsuario=%s, Direccion_idDireccion=%s, Rol_idRol=%s
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
            sql = "DELETE FROM `BD_Libreria`.`Usuario` WHERE idUsuario=%s"
            cursor.execute(sql, (id_usuario,))
        connection.commit()
    finally:
        connection.close()

# Leer todas las direcciones
def read_addresses():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idDireccion, calle, numero FROM `BD_Libreria`.`Direccion`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Leer todos los roles
def read_roles():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idRol, rol FROM `BD_Libreria`.`Rol`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para la tabla Usuario
class UserCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Usuario')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')
        layout.addWidget(self.nombre_input)

        self.apellido_input = QLineEdit(self)
        self.apellido_input.setPlaceholderText('Apellido')
        layout.addWidget(self.apellido_input)

        self.correo_input = QLineEdit(self)
        self.correo_input.setPlaceholderText('Correo Electrónico')
        layout.addWidget(self.correo_input)

        self.telefono_input = QLineEdit(self)
        self.telefono_input.setPlaceholderText('Teléfono')
        layout.addWidget(self.telefono_input)

        self.fecha_nacimiento_input = QDateEdit(self)
        self.fecha_nacimiento_input.setDisplayFormat('yyyy-MM-dd')
        self.fecha_nacimiento_input.setCalendarPopup(True)
        layout.addWidget(self.fecha_nacimiento_input)

        self.imagen_usuario_input = QLineEdit(self)
        self.imagen_usuario_input.setPlaceholderText('URL de Imagen')
        layout.addWidget(self.imagen_usuario_input)

        # ComboBox para seleccionar la dirección
        self.direccion_combobox = QComboBox(self)
        layout.addWidget(self.direccion_combobox)
        self.load_addresses()

        # ComboBox para seleccionar el rol
        self.rol_combobox = QComboBox(self)
        layout.addWidget(self.rol_combobox)
        self.load_roles()

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
        self.table.setHorizontalHeaderLabels(['ID Usuario', 'Nombre', 'Apellido', 'Correo', 'Teléfono', 'Fecha Nacimiento', 'Imagen Usuario', 'ID Dirección', 'ID Rol'])
        for row_idx, user in enumerate(users):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user['idUsuario'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(user['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(user['apellido']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(user['correo']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(user['telefono']))
            self.table.setItem(row_idx, 5, QTableWidgetItem(user['fechaNacimiento'].strftime('%Y-%m-%d') if user['fechaNacimiento'] else ''))
            self.table.setItem(row_idx, 6, QTableWidgetItem(user['imagenUsuario']))
            self.table.setItem(row_idx, 7, QTableWidgetItem(str(user['Direccion_idDireccion'])))
            self.table.setItem(row_idx, 8, QTableWidgetItem(str(user['Rol_idRol'])))

    def load_addresses(self):
        addresses = read_addresses()
        self.direccion_combobox.clear()
        for address in addresses:
            display_text = f"{address['idDireccion']}: {address['calle']} {address['numero']}"
            self.direccion_combobox.addItem(display_text, address['idDireccion'])

    def load_roles(self):
        roles = read_roles()
        self.rol_combobox.clear()
        for role in roles:
            self.rol_combobox.addItem(role['rol'], role['idRol'])

    def create_user(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        correo = self.correo_input.text()
        telefono = self.telefono_input.text()
        fecha_nacimiento = self.fecha_nacimiento_input.date().toString('yyyy-MM-dd')
        imagen_usuario = self.imagen_usuario_input.text()
        direccion_id = self.direccion_combobox.currentData()
        rol_id = self.rol_combobox.currentData()

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
        fecha_nacimiento = self.fecha_nacimiento_input.date().toString('yyyy-MM-dd')
        imagen_usuario = self.imagen_usuario_input.text()
        direccion_id = self.direccion_combobox.currentData()
        rol_id = self.rol_combobox.currentData()

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
    window = UserCRUDApp()
    window.show()
    sys.exit(app.exec_())
