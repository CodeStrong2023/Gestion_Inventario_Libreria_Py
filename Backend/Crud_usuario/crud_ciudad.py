from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QComboBox
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

# Funciones CRUD para la tabla Ciudad

# Crear una nueva ciudad
def create_city(nombre, pais_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `BD_Libreria`.`Ciudad` (nombre, Pais_idPais) VALUES (%s, %s)"
            cursor.execute(sql, (nombre, pais_id))
        connection.commit()
    finally:
        connection.close()

# Leer todas las ciudades
def read_cities():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Ciudad`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Leer todos los países (para el combo box)
def read_countries():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Pais`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Actualizar una ciudad
def update_city(id_ciudad, nombre, pais_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `BD_Libreria`.`Ciudad` SET nombre=%s, Pais_idPais=%s WHERE idCiudad=%s"
            cursor.execute(sql, (nombre, pais_id, id_ciudad))
        connection.commit()
    finally:
        connection.close()

# Eliminar una ciudad
def delete_city(id_ciudad):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Ciudad` WHERE idCiudad=%s"
            cursor.execute(sql, (id_ciudad,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para la tabla Ciudad
class CityCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Ciudad')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre de la Ciudad')
        layout.addWidget(self.nombre_input)

        self.pais_combobox = QComboBox(self)
        self.load_countries()
        layout.addWidget(self.pais_combobox)

        self.create_button = QPushButton('Crear Ciudad', self)
        self.create_button.clicked.connect(self.create_city)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Ciudad', self)
        self.update_button.clicked.connect(self.update_city)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Ciudad', self)
        self.delete_button.clicked.connect(self.delete_city)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_countries(self):
        countries = read_countries()
        for country in countries:
            self.pais_combobox.addItem(country['nombre'], country['idPais'])

    def load_data(self):
        cities = read_cities()
        self.table.setRowCount(len(cities))
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'ID País'])
        for row_idx, city in enumerate(cities):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(city['idCiudad'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(city['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(city['Pais_idPais'])))

    def create_city(self):
        nombre = self.nombre_input.text()
        pais_id = self.pais_combobox.currentData()
        create_city(nombre, pais_id)
        self.load_data()

    def update_city(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una ciudad para actualizar')
            return

        id_ciudad = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        pais_id = self.pais_combobox.currentData()
        update_city(id_ciudad, nombre, pais_id)
        self.load_data()

    def delete_city(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una ciudad para eliminar')
            return

        id_ciudad = int(self.table.item(selected, 0).text())
        delete_city(id_ciudad)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    city_window = CityCRUDApp()
    city_window.show()
    sys.exit(app.exec_())
