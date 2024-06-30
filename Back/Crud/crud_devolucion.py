from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QDateEdit, QComboBox, QMessageBox
from PyQt5.QtCore import QDate
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

# Funciones CRUD para Devolucion
def create_devolucion(motivo, fecha_devolucion, cantidad, pago_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO `BD_Libreria`.`Devolucion` (motivo, fechaDevolucion, cantidad, Pago_idPago)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (motivo, fecha_devolucion, cantidad, pago_id))
        connection.commit()
    finally:
        connection.close()

def read_devoluciones():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Devolucion`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_devolucion(id_devolucion, motivo, fecha_devolucion, cantidad, pago_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Devolucion SET motivo=%s, fechaDevolucion=%s, cantidad=%s, Pago_idPago=%s
            WHERE idDevolucion=%s
            """
            cursor.execute(sql, (motivo, fecha_devolucion, cantidad, pago_id, id_devolucion))
        connection.commit()
    finally:
        connection.close()

def delete_devolucion(id_devolucion, pago_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Devolucion WHERE idDevolucion=%s AND Pago_idPago=%s"
            cursor.execute(sql, (id_devolucion, pago_id))
        connection.commit()
    finally:
        connection.close()

def read_payments():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idPago FROM `BD_Libreria`.`Pago`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Devolucion
class DevolucionCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Devolución')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.motivo_input = QLineEdit(self)
        self.motivo_input.setPlaceholderText('Motivo')
        layout.addWidget(self.motivo_input)

        self.fecha_input = QDateEdit(self)
        self.fecha_input.setCalendarPopup(True)
        self.fecha_input.setDate(QDate.currentDate())
        layout.addWidget(self.fecha_input)

        self.cantidad_input = QLineEdit(self)
        self.cantidad_input.setPlaceholderText('Cantidad')
        layout.addWidget(self.cantidad_input)

        self.pago_input = QComboBox(self)
        self.load_payments()
        layout.addWidget(self.pago_input)

        self.create_button = QPushButton('Crear Devolución', self)
        self.create_button.clicked.connect(self.create_devolucion)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Devolución', self)
        self.update_button.clicked.connect(self.update_devolucion)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Devolución', self)
        self.delete_button.clicked.connect(self.delete_devolucion)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        devoluciones = read_devoluciones()
        self.table.setRowCount(len(devoluciones))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Motivo', 'Fecha Devolución', 'Cantidad', 'ID Pago'])
        for row_idx, devolucion in enumerate(devoluciones):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(devolucion['idDevolucion'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(devolucion['motivo']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(devolucion['fechaDevolucion'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(devolucion['cantidad'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(devolucion['Pago_idPago'])))

    def load_payments(self):
        payments = read_payments()
        self.pago_input.clear()
        for payment in payments:
            self.pago_input.addItem(str(payment['idPago']), payment['idPago'])

    def create_devolucion(self):
        motivo = self.motivo_input.text()
        fecha_devolucion = self.fecha_input.date().toString('yyyy-MM-dd')
        cantidad = int(self.cantidad_input.text())
        pago_id = int(self.pago_input.currentData())

        create_devolucion(motivo, fecha_devolucion, cantidad, pago_id)
        self.load_data()

    def update_devolucion(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una devolución para actualizar')
            return

        id_devolucion = int(self.table.item(selected, 0).text())
        motivo = self.motivo_input.text()
        fecha_devolucion = self.fecha_input.date().toString('yyyy-MM-dd')
        cantidad = int(self.cantidad_input.text())
        pago_id = int(self.pago_input.currentData())

        update_devolucion(id_devolucion, motivo, fecha_devolucion, cantidad, pago_id)
        self.load_data()

    def delete_devolucion(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una devolución para eliminar')
            return

        id_devolucion = int(self.table.item(selected, 0).text())
        pago_id = int(self.table.item(selected, 4).text())
        delete_devolucion(id_devolucion, pago_id)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DevolucionCRUDApp()
    window.show()
    sys.exit(app.exec_())
