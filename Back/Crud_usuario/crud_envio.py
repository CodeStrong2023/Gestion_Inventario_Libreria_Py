from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox, QComboBox
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

# Funciones CRUD para la tabla Envio
def create_shipment(tipo, estado, fecha_despacho, fecha_entrega, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Envio (tipo, estado, fechaDespacho, fechaEntrega, Direccion_idDireccion)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (tipo, estado, fecha_despacho, fecha_entrega, direccion_id))
        connection.commit()
    finally:
        connection.close()

def read_shipments():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Envio")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_shipment(id_envio, tipo, estado, fecha_despacho, fecha_entrega, direccion_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Envio
            SET tipo=%s, estado=%s, fechaDespacho=%s, fechaEntrega=%s, Direccion_idDireccion=%s
            WHERE idEnvio=%s
            """
            cursor.execute(sql, (tipo, estado, fecha_despacho, fecha_entrega, direccion_id, id_envio))
        connection.commit()
    finally:
        connection.close()

def delete_shipment(id_envio):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Envio WHERE idEnvio=%s"
            cursor.execute(sql, (id_envio,))
        connection.commit()
    finally:
        connection.close()

# Función para cargar direcciones
def load_addresses():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idDireccion, calle FROM Direccion")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Envío
class ShipmentCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Envío')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.tipo_input = QLineEdit(self)
        self.tipo_input.setPlaceholderText('Tipo de Envío')
        layout.addWidget(self.tipo_input)

        self.estado_input = QLineEdit(self)
        self.estado_input.setPlaceholderText('Estado')
        layout.addWidget(self.estado_input)

        self.fecha_despacho_input = QLineEdit(self)
        self.fecha_despacho_input.setPlaceholderText('Fecha de Despacho (YYYY-MM-DD)')
        layout.addWidget(self.fecha_despacho_input)

        self.fecha_entrega_input = QLineEdit(self)
        self.fecha_entrega_input.setPlaceholderText('Fecha de Entrega (YYYY-MM-DD)')
        layout.addWidget(self.fecha_entrega_input)

        self.direccion_combo = QComboBox(self)
        self.load_addresses()
        layout.addWidget(self.direccion_combo)

        self.create_button = QPushButton('Crear Envío', self)
        self.create_button.clicked.connect(self.create_shipment)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Envío', self)
        self.update_button.clicked.connect(self.update_shipment)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Envío', self)
        self.delete_button.clicked.connect(self.delete_shipment)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        shipments = read_shipments()
        self.table.setRowCount(len(shipments))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Tipo', 'Estado', 'Fecha de Despacho', 'Fecha de Entrega', 'ID Dirección'])
        for row_idx, shipment in enumerate(shipments):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(shipment['idEnvio'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(shipment['tipo']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(shipment['estado']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(shipment['fechaDespacho'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(shipment['fechaEntrega'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(shipment['Direccion_idDireccion'])))

    def load_addresses(self):
        addresses = load_addresses()
        self.direccion_combo.clear()
        for address in addresses:
            self.direccion_combo.addItem(f"{address['calle']} (ID: {address['idDireccion']})", address['idDireccion'])

    def create_shipment(self):
        tipo = self.tipo_input.text()
        estado = self.estado_input.text()
        fecha_despacho = self.fecha_despacho_input.text()
        fecha_entrega = self.fecha_entrega_input.text()
        direccion_id = self.direccion_combo.currentData()

        create_shipment(tipo, estado, fecha_despacho, fecha_entrega, direccion_id)
        self.load_data()

    def update_shipment(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un envío para actualizar')
            return

        id_envio = int(self.table.item(selected, 0).text())
        tipo = self.tipo_input.text()
        estado = self.estado_input.text()
        fecha_despacho = self.fecha_despacho_input.text()
        fecha_entrega = self.fecha_entrega_input.text()
        direccion_id = self.direccion_combo.currentData()

        update_shipment(id_envio, tipo, estado, fecha_despacho, fecha_entrega, direccion_id)
        self.load_data()

    def delete_shipment(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un envío para eliminar')
            return

        id_envio = int(self.table.item(selected, 0).text())
        delete_shipment(id_envio)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShipmentCRUDApp()
    window.show()
    sys.exit(app.exec_())
