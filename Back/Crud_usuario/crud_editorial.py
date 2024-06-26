from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox, QFileDialog
import sys
import pymysql

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',   # Dirección del servidor MySQL
        user='root',        # Usuario de MySQL
        password='contraseña', # Contraseña de MySQL
        database='BD_Libreria',   # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Funciones CRUD para la tabla Editorial
def create_editorial(nombre, imagen_editorial):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO `BD_Libreria`.`Editorial` (nombre, imagenEditorial)
            VALUES (%s, %s)
            """
            cursor.execute(sql, (nombre, imagen_editorial))
        connection.commit()
    finally:
        connection.close()

def read_editorials():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Editorial`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_editorial(id_editorial, nombre, imagen_editorial):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Editorial SET nombre=%s, imagenEditorial=%s
            WHERE idEditorial=%s
            """
            cursor.execute(sql, (nombre, imagen_editorial, id_editorial))
        connection.commit()
    finally:
        connection.close()

def delete_editorial(id_editorial):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Editorial WHERE idEditorial=%s"
            cursor.execute(sql, (id_editorial,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Editorial
class EditorialCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Editorial')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')
        layout.addWidget(self.nombre_input)

        self.imagen_editorial_input = QLineEdit(self)
        self.imagen_editorial_input.setReadOnly(True)
        self.imagen_editorial_input.setPlaceholderText('Imagen Editorial')
        layout.addWidget(self.imagen_editorial_input)

        self.select_image_button = QPushButton('Seleccionar Imagen', self)
        self.select_image_button.clicked.connect(self.select_image)
        layout.addWidget(self.select_image_button)

        self.create_button = QPushButton('Crear Editorial', self)
        self.create_button.clicked.connect(self.create_editorial)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Editorial', self)
        self.update_button.clicked.connect(self.update_editorial)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Editorial', self)
        self.delete_button.clicked.connect(self.delete_editorial)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        editorials = read_editorials()
        self.table.setRowCount(len(editorials))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Imagen Editorial'])
        for row_idx, editorial in enumerate(editorials):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(editorial['idEditorial'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(editorial['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(editorial['imagenEditorial']))

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.gif)", options=options)
        if file_name:
            self.imagen_editorial_input.setText(file_name)

    def create_editorial(self):
        nombre = self.nombre_input.text()
        imagen_editorial = self.imagen_editorial_input.text()

        create_editorial(nombre, imagen_editorial)
        self.load_data()

    def update_editorial(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una editorial para actualizar')
            return

        id_editorial = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        imagen_editorial = self.imagen_editorial_input.text()

        update_editorial(id_editorial, nombre, imagen_editorial)
        self.load_data()

    def delete_editorial(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una editorial para eliminar')
            return

        id_editorial = int(self.table.item(selected, 0).text())
        delete_editorial(id_editorial)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditorialCRUDApp()
    window.show()
    sys.exit(app.exec_())
