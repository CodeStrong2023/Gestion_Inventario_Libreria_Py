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

# Funciones CRUD para la tabla Empresa

# Crear una nueva empresa
def create_company(nombre, telefono, correo, cuil, logo_empresa, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO `BD_Libreria`.`Empresa` (nombre, telefono, correo, cuil, logoEmpresa, Direccion_idDireccion)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nombre, telefono, correo, cuil, logo_empresa, direccion_id))
        connection.commit()
    finally:
        connection.close()

# Leer todas las empresas
def read_companies():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Empresa`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Actualizar una empresa
def update_company(id_empresa, nombre, telefono, correo, cuil, logo_empresa, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE `BD_Libreria`.`Empresa`
            SET nombre=%s, telefono=%s, correo=%s, cuil=%s, logoEmpresa=%s, Direccion_idDireccion=%s
            WHERE idEmpresa=%s
            """
            cursor.execute(sql, (nombre, telefono, correo, cuil, logo_empresa, direccion_id, id_empresa))
        connection.commit()
    finally:
        connection.close()

# Eliminar una empresa
def delete_company(id_empresa):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Empresa` WHERE idEmpresa=%s"
            cursor.execute(sql, (id_empresa,))
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

# Aplicación PyQt5 para la tabla Empresa
class CompanyCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Empresa')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre de la Empresa')
        layout.addWidget(self.nombre_input)

        self.telefono_input = QLineEdit(self)
        self.telefono_input.setPlaceholderText('Teléfono')
        layout.addWidget(self.telefono_input)

        self.correo_input = QLineEdit(self)
        self.correo_input.setPlaceholderText('Correo Electrónico')
        layout.addWidget(self.correo_input)

        self.cuil_input = QLineEdit(self)
        self.cuil_input.setPlaceholderText('CUIL')
        layout.addWidget(self.cuil_input)

        self.logo_empresa_input = QLineEdit(self)
        self.logo_empresa_input.setPlaceholderText('Logo de la Empresa')
        layout.addWidget(self.logo_empresa_input)

        # ComboBox para seleccionar la dirección
        self.direccion_combobox = QComboBox(self)
        layout.addWidget(self.direccion_combobox)
        self.load_addresses()

        self.create_button = QPushButton('Crear Empresa', self)
        self.create_button.clicked.connect(self.create_company)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Empresa', self)
        self.update_button.clicked.connect(self.update_company)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Empresa', self)
        self.delete_button.clicked.connect(self.delete_company)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        companies = read_companies()
        self.table.setRowCount(len(companies))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID Empresa', 'Nombre', 'Teléfono', 'Correo', 'CUIL', 'Logo Empresa', 'ID Dirección'])
        for row_idx, company in enumerate(companies):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(company['idEmpresa'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(company['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(company['telefono']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(company['correo']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(company['cuil'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(company['logoEmpresa']))
            self.table.setItem(row_idx, 6, QTableWidgetItem(str(company['Direccion_idDireccion'])))

    def load_addresses(self):
        addresses = read_addresses()
        self.direccion_combobox.clear()
        for address in addresses:
            display_text = f"{address['idDireccion']}: {address['calle']} {address['numero']}"
            self.direccion_combobox.addItem(display_text, address['idDireccion'])

    def create_company(self):
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        correo = self.correo_input.text()
        cuil = self.cuil_input.text()
        logo_empresa = self.logo_empresa_input.text()
        direccion_id = self.direccion_combobox.currentData()

        create_company(nombre, telefono, correo, cuil, logo_empresa, direccion_id)
        self.load_data()

    def update_company(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una empresa para actualizar')
            return

        id_empresa = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        correo = self.correo_input.text()
        cuil = self.cuil_input.text()
        logo_empresa = self.logo_empresa_input.text()
        direccion_id = self.direccion_combobox.currentData()

        update_company(id_empresa, nombre, telefono, correo, cuil, logo_empresa, direccion_id)
        self.load_data()

    def delete_company(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una empresa para eliminar')
            return

        id_empresa = int(self.table.item(selected, 0).text())
        delete_company(id_empresa)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    company_window = CompanyCRUDApp()
    company_window.show()
    sys.exit(app.exec_())

