from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QComboBox
import sys
import pymysql

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',  
        user='root',       
        password='contraseña',  
        database='BD_Libreria',  
        cursorclass=pymysql.cursors.DictCursor  
    )

# Funciones CRUD para la tabla Almacenamiento
def create_storage(capacidad_total, uso, empresa_id, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Almacenamiento (capacidadTotalM3, usoM3, Empresa_idEmpresa, Direccion_idDireccion)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (capacidad_total, uso, empresa_id, direccion_id))
        connection.commit()
    finally:
        connection.close()

def read_storages():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Almacenamiento")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_storage(id_almacenamiento, capacidad_total, uso, empresa_id, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Almacenamiento
            SET capacidadTotalM3=%s, usoM3=%s, Empresa_idEmpresa=%s, Direccion_idDireccion=%s
            WHERE idAlmacenamiento=%s
            """
            cursor.execute(sql, (capacidad_total, uso, empresa_id, direccion_id, id_almacenamiento))
        connection.commit()
    finally:
        connection.close()

def delete_storage(id_almacenamiento):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Almacenamiento WHERE idAlmacenamiento=%s"
            cursor.execute(sql, (id_almacenamiento,))
        connection.commit()
    finally:
        connection.close()

# Funciones para cargar empresas y direcciones
def load_companies():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idEmpresa, nombre FROM Empresa")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def load_addresses():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idDireccion, calle FROM Direccion")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Almacenamiento
class StorageCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Almacenamiento')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campo de entrada y botones
        self.capacidad_input = QLineEdit(self)
        self.capacidad_input.setPlaceholderText('Capacidad Total (m³)')
        layout.addWidget(self.capacidad_input)

        self.uso_input = QLineEdit(self)
        self.uso_input.setPlaceholderText('Uso (m³)')
        layout.addWidget(self.uso_input)

        self.empresa_combo = QComboBox(self)
        self.load_companies()
        layout.addWidget(self.empresa_combo)

        self.direccion_combo = QComboBox(self)
        self.load_addresses()
        layout.addWidget(self.direccion_combo)

        self.create_button = QPushButton('Crear Almacenamiento', self)
        self.create_button.clicked.connect(self.create_storage)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Almacenamiento', self)
        self.update_button.clicked.connect(self.update_storage)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Almacenamiento', self)
        self.delete_button.clicked.connect(self.delete_storage)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        storages = read_storages()
        self.table.setRowCount(len(storages))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Capacidad Total', 'Uso', 'ID Empresa', 'ID Dirección'])
        for row_idx, storage in enumerate(storages):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(storage['idAlmacenamiento'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(storage['capacidadTotalM3']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(storage['usoM3']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(storage['Empresa_idEmpresa'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(storage['Direccion_idDireccion'])))

    def load_companies(self):
        companies = load_companies()
        self.empresa_combo.clear()
        for company in companies:
            self.empresa_combo.addItem(f"{company['nombre']} (ID: {company['idEmpresa']})", company['idEmpresa'])

    def load_addresses(self):
        addresses = load_addresses()
        self.direccion_combo.clear()
        for address in addresses:
            self.direccion_combo.addItem(f"{address['calle']} (ID: {address['idDireccion']})", address['idDireccion'])

    def create_storage(self):
        capacidad_total = self.capacidad_input.text()
        uso = self.uso_input.text()
        empresa_id = self.empresa_combo.currentData()
        direccion_id = self.direccion_combo.currentData()

        create_storage(capacidad_total, uso, empresa_id, direccion_id)
        self.load_data()

    def update_storage(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un almacenamiento para actualizar')
            return

        id_almacenamiento = int(self.table.item(selected, 0).text())
        capacidad_total = self.capacidad_input.text()
        uso = self.uso_input.text()
        empresa_id = self.empresa_combo.currentData()
        direccion_id = self.direccion_combo.currentData()

        update_storage(id_almacenamiento, capacidad_total, uso, empresa_id, direccion_id)
        self.load_data()

    def delete_storage(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un almacenamiento para eliminar')
            return

        id_almacenamiento = int(self.table.item(selected, 0).text())
        delete_storage(id_almacenamiento)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StorageCRUDApp()
    window.show()
    sys.exit(app.exec_())