from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox, QFileDialog
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

# Funciones CRUD para la tabla Facturas
def create_invoice(tipo, fecha_emision, imagen_factura):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Facturas (tipo, fechaEmision, imagenFactura)
            VALUES (%s, %s, %s)
            """
            cursor.execute(sql, (tipo, fecha_emision, imagen_factura))
        connection.commit()
    finally:
        connection.close()

def read_invoices():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Facturas")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_invoice(id_factura, tipo, fecha_emision, imagen_factura):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Facturas
            SET tipo=%s, fechaEmision=%s, imagenFactura=%s
            WHERE idFacturas=%s
            """
            cursor.execute(sql, (tipo, fecha_emision, imagen_factura, id_factura))
        connection.commit()
    finally:
        connection.close()

def delete_invoice(id_factura):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Facturas WHERE idFacturas=%s"
            cursor.execute(sql, (id_factura,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Facturas
class InvoiceCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Facturas')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.tipo_input = QLineEdit(self)
        self.tipo_input.setPlaceholderText('Tipo de Factura')
        layout.addWidget(self.tipo_input)

        self.fecha_emision_input = QLineEdit(self)
        self.fecha_emision_input.setPlaceholderText('Fecha de Emisión (YYYY-MM-DD)')
        layout.addWidget(self.fecha_emision_input)

        self.imagen_factura_label = QLabel('Seleccionar Imagen:')
        layout.addWidget(self.imagen_factura_label)

        self.imagen_factura_path = ''
        self.select_image_button = QPushButton('Seleccionar Imagen', self)
        self.select_image_button.clicked.connect(self.select_image)
        layout.addWidget(self.select_image_button)

        self.create_button = QPushButton('Crear Factura', self)
        self.create_button.clicked.connect(self.create_invoice)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Factura', self)
        self.update_button.clicked.connect(self.update_invoice)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Factura', self)
        self.delete_button.clicked.connect(self.delete_invoice)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        invoices = read_invoices()
        self.table.setRowCount(len(invoices))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', 'Tipo', 'Fecha de Emisión', 'Imagen de Factura'])
        for row_idx, invoice in enumerate(invoices):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(invoice['idFacturas'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(invoice['tipo']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(invoice['fechaEmision'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(invoice['imagenFactura']))

    def select_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen de Factura", "", "Image Files (*.png *.jpg *.jpeg *.gif)", options=options)
        if file_path:
            self.imagen_factura_path = file_path
            self.imagen_factura_label.setText(f'Imagen seleccionada: {file_path}')

    def create_invoice(self):
        tipo = self.tipo_input.text()
        fecha_emision = self.fecha_emision_input.text()
        imagen_factura = self.imagen_factura_path

        create_invoice(tipo, fecha_emision, imagen_factura)
        self.load_data()

    def update_invoice(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una factura para actualizar')
            return

        id_factura = int(self.table.item(selected, 0).text())
        tipo = self.tipo_input.text()
        fecha_emision = self.fecha_emision_input.text()
        imagen_factura = self.imagen_factura_path

        update_invoice(id_factura, tipo, fecha_emision, imagen_factura)
        self.load_data()

    def delete_invoice(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una factura para eliminar')
            return

        id_factura = int(self.table.item(selected, 0).text())
        delete_invoice(id_factura)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InvoiceCRUDApp()
    window.show()
    sys.exit(app.exec_())
