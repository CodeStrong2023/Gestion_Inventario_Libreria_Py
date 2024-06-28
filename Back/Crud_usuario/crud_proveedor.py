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

# Funciones CRUD para Proveedor
def create_provider(nombre, telefono, contacto_principal):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO `BD_Libreria`.`Proveedor` (nombre, telefono, contactoPrincipal)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (nombre, telefono, contacto_principal))
        connection.commit()
    finally:
        connection.close()

def read_providers():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Proveedor`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_provider(id_proveedor, nombre, telefono, contacto_principal):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Proveedor SET nombre=%s, telefono=%s, contactoPrincipal=%s
            WHERE idProveedor=%s
            """
            cursor.execute(sql, (nombre, telefono, contacto_principal, id_proveedor))
        connection.commit()
    finally:
        connection.close()

def delete_provider(id_proveedor):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Proveedor WHERE idProveedor=%s"
            cursor.execute(sql, (id_proveedor,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Proveedor
class ProveedorCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Proveedor')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.nombre_input = QLineEdit(self)
        self.nombre_input.setPlaceholderText('Nombre')
        layout.addWidget(self.nombre_input)

        self.telefono_input = QLineEdit(self)
        self.telefono_input.setPlaceholderText('Teléfono')
        layout.addWidget(self.telefono_input)

        self.contacto_principal_input = QLineEdit(self)
        self.contacto_principal_input.setPlaceholderText('Contacto Principal')
        layout.addWidget(self.contacto_principal_input)

        self.create_button = QPushButton('Crear Proveedor', self)
        self.create_button.clicked.connect(self.create_provider)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Proveedor', self)
        self.update_button.clicked.connect(self.update_provider)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Proveedor', self)
        self.delete_button.clicked.connect(self.delete_provider)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        providers = read_providers()
        self.table.setRowCount(len(providers))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Teléfono', 'Contacto Principal'])
        for row_idx, provider in enumerate(providers):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(provider['idProveedor'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(provider['nombre']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(provider['telefono']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(provider['contactoPrincipal']))

    def create_provider(self):
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        contacto_principal = self.contacto_principal_input.text()

        create_provider(nombre, telefono, contacto_principal)
        self.load_data()

    def update_provider(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un proveedor para actualizar')
            return

        id_proveedor = int(self.table.item(selected, 0).text())
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        contacto_principal = self.contacto_principal_input.text()

        update_provider(id_proveedor, nombre, telefono, contacto_principal)
        self.load_data()

    def delete_provider(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un proveedor para eliminar')
            return

        id_proveedor = int(self.table.item(selected, 0).text())
        delete_provider(id_proveedor)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProveedorCRUDApp()
    window.show()
    sys.exit(app.exec_())
