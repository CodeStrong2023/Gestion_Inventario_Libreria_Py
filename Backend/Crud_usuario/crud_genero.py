from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox
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

# Funciones CRUD para Genero
def create_genero(nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `BD_Libreria`.`genero` (nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
        connection.commit()
    finally:
        connection.close()

def read_generos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`genero`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_genero(id_genero, nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `BD_Libreria`.`genero` SET nombre=%s WHERE idgenero=%s"
            cursor.execute(sql, (nombre, id_genero))
        connection.commit()
    finally:
        connection.close()

def delete_genero(id_genero):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`genero` WHERE idgenero=%s"
            cursor.execute(sql, (id_genero,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Genero
class GeneroCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Género')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre del Género')
        layout.addWidget(self.nombre_input)

        self.create_button = QPushButton('Crear Género', self)
        self.create_button.clicked.connect(self.create_genero)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Género', self)
        self.update_button.clicked.connect(self.update_genero)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Género', self)
        self.delete_button.clicked.connect(self.delete_genero)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        generos = read_generos()
        self.table.setRowCount(len(generos))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre'])
        for row_idx, genero in enumerate(generos):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(genero['idgenero'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(genero['nombre']))

    def create_genero(self):
        nombre = self.nombre_input.text()
        if not nombre:
            QMessageBox.warning(self, 'Error', 'El campo "Nombre" no puede estar vacío')
            return
        create_genero(nombre)
        self.load_data()
        self.nombre_input.clear()

    def update_genero(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un género para actualizar')
            return

        id_genero = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        if not nombre:
            QMessageBox.warning(self, 'Error', 'El campo "Nombre" no puede estar vacío')
            return

        update_genero(id_genero, nombre)
        self.load_data()
        self.nombre_input.clear()

    def delete_genero(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un género para eliminar')
            return

        id_genero = int(self.table.item(selected, 0).text())
        delete_genero(id_genero)
        self.load_data()
        self.nombre_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GeneroCRUDApp()
    window.show()
    sys.exit(app.exec_())
