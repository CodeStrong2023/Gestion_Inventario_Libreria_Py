from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QComboBox, QDateEdit, QFileDialog
import sys
import pymysql

# Función para conectar a la base de datos MySQL
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
        connection.commit()  # Confirmar la transacción
    finally:
        connection.close()

# Leer todos los usuarios
def read_users():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Usuario`")
            result = cursor.fetchall()  # Obtener todos los resultados
            return result
    finally:
        connection.close()

# Actualizar un usuario existente
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
        connection.commit()  # Confirmar la transacción
    finally:
        connection.close()

# Eliminar un usuario
def delete_user(id_usuario):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Usuario` WHERE idUsuario=%s"
            cursor.execute(sql, (id_usuario,))
        connection.commit()  # Confirmar la transacción
    finally:
        connection.close()

# Leer todas las direcciones disponibles
def read_addresses():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idDireccion, calle, numero FROM `BD_Libreria`.`Direccion`")
            result = cursor.fetchall()  # Obtener todos los resultados
            return result
    finally:
        connection.close()

# Leer todos los roles disponibles
def read_roles():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idRol, rol FROM `BD_Libreria`.`Rol`")
            result = cursor.fetchall()  # Obtener todos los resultados
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para la tabla Usuario
class UserCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Inicializa la interfaz de usuario

    def initUI(self):
        self.setWindowTitle('CRUD de Usuario')  # Título de la ventana
        self.setGeometry(100, 100, 800, 600)  # Dimensiones de la ventana

        layout = QVBoxLayout()  # Layout vertical principal para la ventana

        # Campos de entrada para los datos del usuario
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')  # Texto de ayuda en el campo
        layout.addWidget(self.nombre_input)  # Añadir el campo al layout

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
        self.fecha_nacimiento_input.setDisplayFormat('yyyy-MM-dd')  # Formato de la fecha
        self.fecha_nacimiento_input.setCalendarPopup(True)  # Mostrar calendario emergente
        layout.addWidget(self.fecha_nacimiento_input)

        # Etiqueta y botón para seleccionar la imagen del usuario
        self.imagen_usuario_label = QLabel('Seleccionar Imagen de Usuario:')
        layout.addWidget(self.imagen_usuario_label)

        self.imagen_usuario_path = ''  # Variable para almacenar la ruta de la imagen seleccionada
        self.select_image_button = QPushButton('Seleccionar Imagen', self)
        self.select_image_button.clicked.connect(self.select_image)  # Conectar el botón para seleccionar la imagen
        layout.addWidget(self.select_image_button)

        # ComboBox para seleccionar la dirección de un usuario
        self.direccion_combobox = QComboBox(self)
        layout.addWidget(self.direccion_combobox)
        self.load_addresses()  # Cargar direcciones disponibles en el ComboBox

        # ComboBox para seleccionar el rol de un usuario
        self.rol_combobox = QComboBox(self)
        layout.addWidget(self.rol_combobox)
        self.load_roles()  # Cargar roles disponibles en el ComboBox

        # Botón para crear un nuevo usuario
        self.create_button = QPushButton('Crear Usuario', self)
        self.create_button.clicked.connect(self.create_user)  # Conectar el evento de clic con la función create_user
        layout.addWidget(self.create_button)

        # Botón para actualizar un usuario existente
        self.update_button = QPushButton('Actualizar Usuario', self)
        self.update_button.clicked.connect(self.update_user)  # Conectar el evento de clic con la función update_user
        layout.addWidget(self.update_button)

        # Botón para eliminar un usuario seleccionado
        self.delete_button = QPushButton('Eliminar Usuario', self)
        self.delete_button.clicked.connect(self.delete_user)  # Conectar el evento de clic con la función delete_user
        layout.addWidget(self.delete_button)

        # Tabla para mostrar la lista de usuarios
        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)  # Establecer el layout principal para la ventana
        self.load_data()  # Cargar datos iniciales en la tabla

    # Cargar los datos de los usuarios en la tabla
    def load_data(self):
        users = read_users()  # Leer los datos de los usuarios desde la base de datos
        self.table.setRowCount(len(users))  # Establecer el número de filas de la tabla
        self.table.setColumnCount(9)  # Establecer el número de columnas de la tabla
        self.table.setHorizontalHeaderLabels(['ID Usuario', 'Nombre', 'Apellido', 'Correo', 'Teléfono', 'Fecha Nacimiento', 'Imagen Usuario', 'ID Dirección', 'ID Rol'])
        
        # Rellenar la tabla con los datos de los usuarios
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

    # Cargar las direcciones disponibles en el ComboBox
    def load_addresses(self):
        addresses = read_addresses()  # Leer las direcciones desde la base de datos
        self.direccion_combobox.clear()  # Limpiar el ComboBox
        for address in addresses:
            display_text = f"{address['idDireccion']}: {address['calle']} {address['numero']}"
            self.direccion_combobox.addItem(display_text, address['idDireccion'])  # Añadir cada dirección al ComboBox

    # Cargar los roles disponibles en el ComboBox
    def load_roles(self):
        roles = read_roles()  # Leer los roles desde la base de datos
        self.rol_combobox.clear()  # Limpiar el ComboBox
        for role in roles:
            self.rol_combobox.addItem(role['rol'], role['idRol'])  # Añadir cada rol al ComboBox

    # Selección de imagen de usuario
    def select_image(self):
        options = QFileDialog.Options()  # Opciones para el diálogo de archivo
        # Abrir el diálogo para seleccionar un archivo de imagen
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen de Usuario", "", "Image Files (*.png *.jpg *.jpeg *.gif)", options=options)
        if file_path:  # Si se selecciona una imagen
            self.imagen_usuario_path = file_path  # Almacenar la ruta de la imagen seleccionada
            self.imagen_usuario_label.setText(f'Imagen seleccionada: {file_path}')  # Actualizar la etiqueta para mostrar la ruta de la imagen

    # Crear un nuevo usuario
    def create_user(self):
        # Obtener los valores de los campos de entrada
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        correo = self.correo_input.text()
        telefono = self.telefono_input.text()
        fecha_nacimiento = self.fecha_nacimiento_input.date().toString('yyyy-MM-dd')
        imagen_usuario = self.imagen_usuario_path  # Usar la ruta de la imagen seleccionada
        direccion_id = self.direccion_combobox.currentData()
        rol_id = self.rol_combobox.currentData()

        create_user(nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id)  # Crear usuario en la base de datos
        self.load_data()  # Recargar los datos de la tabla

    # Actualizar un usuario existente
    def update_user(self):
        selected = self.table.currentRow()  # Obtener la fila seleccionada en la tabla
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un usuario para actualizar')  # Mostrar mensaje de error si no hay fila seleccionada
            return

        # Obtener los valores de los campos de entrada y el ID del usuario seleccionado
        id_usuario = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        correo = self.correo_input.text()
        telefono = self.telefono_input.text()
        fecha_nacimiento = self.fecha_nacimiento_input.date().toString('yyyy-MM-dd')
        imagen_usuario = self.imagen_usuario_path  # Usar la ruta de la imagen seleccionada
        direccion_id = self.direccion_combobox.currentData()
        rol_id = self.rol_combobox.currentData()

        update_user(id_usuario, nombre, apellido, correo, telefono, fecha_nacimiento, imagen_usuario, direccion_id, rol_id)  # Actualizar usuario en la base de datos
        self.load_data()  # Recargar los datos de la tabla

    # Eliminar un usuario seleccionado
    def delete_user(self):
        selected = self.table.currentRow()  # Obtener la fila seleccionada en la tabla
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un usuario para eliminar')  # Mostrar mensaje de error si no hay fila seleccionada
            return

        id_usuario = int(self.table.item(selected, 0).text())  # Obtener el ID del usuario seleccionado
        delete_user(id_usuario)  # Eliminar usuario de la base de datos
        self.load_data()  # Recargar los datos de la tabla

# Punto de entrada principal para la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crear la aplicación PyQt5
    window = UserCRUDApp()  # Crear la ventana de la aplicación
    window.show()  # Mostrar la ventana
    sys.exit(app.exec_())  # Ejecutar el ciclo de eventos de la aplicación
