from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox, QFileDialog
import sys
import pymysql

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',    # Dirección del servidor MySQL
        user='root',         # Usuario de MySQL
        password='contraseña',  # Contraseña de MySQL
        database='BD_Libreria',    # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Funciones CRUD para Autor
def create_autor(nombre, apellido, imagen_autor):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `BD_Libreria`.`Autor` (nombre, apellido, imagenAutor) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, apellido, imagen_autor))
        connection.commit()
    finally:
        connection.close()

def read_autores():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Autor`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_autor(id_autor, nombre, apellido, imagen_autor):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `BD_Libreria`.`Autor` SET nombre=%s, apellido=%s, imagenAutor=%s WHERE idAutor=%s"
            cursor.execute(sql, (nombre, apellido, imagen_autor, id_autor))
        connection.commit()
    finally:
        connection.close()

def delete_autor(id_autor):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Autor` WHERE idAutor=%s"
            cursor.execute(sql, (id_autor,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Autor
class AutorCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Autor')
        self.setGeometry(100, 100, 700, 400)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre del Autor')
        layout.addWidget(self.nombre_input)

        self.apellido_input = QLineEdit(self)
        self.apellido_input.setPlaceholderText('Apellido del Autor')
        layout.addWidget(self.apellido_input)

        self.imagen_input = QLineEdit(self)
        self.imagen_input.setPlaceholderText('Ruta de la Imagen del Autor')
        layout.addWidget(self.imagen_input)

        self.browse_button = QPushButton('Buscar Imagen', self)
        self.browse_button.clicked.connect(self.browse_image)
        layout.addWidget(self.browse_button)

        self.create_button = QPushButton('Crear Autor', self)
        self.create_button.clicked.connect(self.create_autor)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Autor', self)
        self.update_button.clicked.connect(self.update_autor)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Autor', self)
        self.delete_button.clicked.connect(self.delete_autor)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        autores = read_autores()
        self.table.setRowCount(len(autores))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido', 'Imagen'])
        for row_idx, autor in enumerate(autores):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(autor['idAutor'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(autor['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(autor['apellido']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(autor['imagenAutor']))

    def browse_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "Imagenes (*.png *.xpm *.jpg *.jpeg);;Todos los archivos (*)", options=options)
        if file_path:
            self.imagen_input.setText(file_path)

    def create_autor(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        imagen_autor = self.imagen_input.text()
        if not nombre or not apellido:
            QMessageBox.warning(self, 'Error', 'Los campos "Nombre" y "Apellido" no pueden estar vacíos')
            return
        create_autor(nombre, apellido, imagen_autor)
        self.load_data()
        self.clear_inputs()

    def update_autor(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un autor para actualizar')
            return

        id_autor = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        imagen_autor = self.imagen_input.text()
        if not nombre or not apellido:
            QMessageBox.warning(self, 'Error', 'Los campos "Nombre" y "Apellido" no pueden estar vacíos')
            return

        update_autor(id_autor, nombre, apellido, imagen_autor)
        self.load_data()
        self.clear_inputs()

    def delete_autor(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un autor para eliminar')
            return

        id_autor = int(self.table.item(selected, 0).text())
        delete_autor(id_autor)
        self.load_data()
        self.clear_inputs()

    def clear_inputs(self):
        self.nombre_input.clear()
        self.apellido_input.clear()
        self.imagen_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutorCRUDApp()
    window.show()
    sys.exit(app.exec_())
