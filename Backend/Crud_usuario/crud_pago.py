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

# Funciones CRUD para la tabla Pago
def create_payment(tipo, cuotas, id_factura, origen):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Pago (tipo, cuotas, Facturas_idFacturas, origen)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (tipo, cuotas, id_factura, origen))
        connection.commit()
    finally:
        connection.close()

def read_payments():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Pago")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_payment(id_pago, tipo, cuotas, id_factura, origen):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Pago
            SET tipo=%s, cuotas=%s, Facturas_idFacturas=%s, origen=%s
            WHERE idPago=%s
            """
            cursor.execute(sql, (tipo, cuotas, id_factura, origen, id_pago))
        connection.commit()
    finally:
        connection.close()

def delete_payment(id_pago):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Pago WHERE idPago=%s"
            cursor.execute(sql, (id_pago,))
        connection.commit()
    finally:
        connection.close()

def load_invoices_combo(combo_box):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idFacturas FROM Facturas")
            result = cursor.fetchall()
            for row in result:
                combo_box.addItem(str(row['idFacturas']))
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Pago
class PaymentCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Pagos')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y ComboBox
        self.tipo_input = QLineEdit(self)
        self.tipo_input.setPlaceholderText('Tipo de Pago')
        layout.addWidget(self.tipo_input)

        self.cuotas_input = QLineEdit(self)
        self.cuotas_input.setPlaceholderText('Número de Cuotas')
        layout.addWidget(self.cuotas_input)

        self.facturas_combo = QComboBox(self)
        self.facturas_combo.addItem("Seleccionar Factura")
        load_invoices_combo(self.facturas_combo)
        layout.addWidget(self.facturas_combo)

        self.origen_input = QLineEdit(self)
        self.origen_input.setPlaceholderText('Origen (Compra/Venta)')
        layout.addWidget(self.origen_input)

        self.create_button = QPushButton('Crear Pago', self)
        self.create_button.clicked.connect(self.create_payment)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Pago', self)
        self.update_button.clicked.connect(self.update_payment)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Pago', self)
        self.delete_button.clicked.connect(self.delete_payment)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        payments = read_payments()
        self.table.setRowCount(len(payments))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Tipo', 'Cuotas', 'ID Factura', 'Origen'])
        for row_idx, payment in enumerate(payments):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(payment['idPago'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(payment['tipo']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(payment['cuotas'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(payment['Facturas_idFacturas'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(payment['origen']))

    def create_payment(self):
        tipo = self.tipo_input.text()
        cuotas = int(self.cuotas_input.text())
        id_factura = int(self.facturas_combo.currentText())
        origen = self.origen_input.text()

        create_payment(tipo, cuotas, id_factura, origen)
        self.load_data()

    def update_payment(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un pago para actualizar')
            return

        id_pago = int(self.table.item(selected, 0).text())
        tipo = self.tipo_input.text()
        cuotas = int(self.cuotas_input.text())
        id_factura = int(self.facturas_combo.currentText())
        origen = self.origen_input.text()

        update_payment(id_pago, tipo, cuotas, id_factura, origen)
        self.load_data()

    def delete_payment(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un pago para eliminar')
            return

        id_pago = int(self.table.item(selected, 0).text())
        delete_payment(id_pago)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaymentCRUDApp()
    window.show()
    sys.exit(app.exec_())
