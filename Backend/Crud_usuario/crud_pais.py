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

# Funciones CRUD para la tabla Pais

# Crear un nuevo país
def create_country(nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `BD_Libreria`.`Pais` (nombre) VALUES (%s)"
            cursor.execute(sql, (nombre,))
        connection.commit()
    finally:
        connection.close()

# Leer todos los países
def read_countries():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Pais`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Actualizar un país
def update_country(id_pais, nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `BD_Libreria`.`Pais` SET nombre=%s WHERE idPais=%s"
            cursor.execute(sql, (nombre, id_pais))
        connection.commit()
    finally:
        connection.close()

# Eliminar un país
def delete_country(id_pais):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Pais` WHERE idPais=%s"
            cursor.execute(sql, (id_pais,))
        connection.commit()
    finally:
        connection.close()

class CountryCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Pais')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre del País')
        layout.addWidget(self.nombre_input)

        self.create_button = QPushButton('Crear País', self)
        self.create_button.clicked.connect(self.create_country)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar País', self)
        self.update_button.clicked.connect(self.update_country)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar País', self)
        self.delete_button.clicked.connect(self.delete_country)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        countries = read_countries()
        self.table.setRowCount(len(countries))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre'])
        for row_idx, country in enumerate(countries):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(country['idPais'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(country['nombre']))

    def create_country(self):
        nombre = self.nombre_input.text()
        create_country(nombre)
        self.load_data()

    def update_country(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un país para actualizar')
            return

        id_pais = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        update_country(id_pais, nombre)
        self.load_data()

    def delete_country(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un país para eliminar')
            return

        id_pais = int(self.table.item(selected, 0).text())
        delete_country(id_pais)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    country_window = CountryCRUDApp()
    country_window.show()
    sys.exit(app.exec_())