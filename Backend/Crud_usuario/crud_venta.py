from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QComboBox, QLabel, QLineEdit, QMessageBox
import sys
import pymysql

# Importaciones de CRUDs personalizados
from crud_users import read_users
from crud_envio import read_shipments
from crud_articulo import read_articles
from crud_pago import read_payments

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',  # Dirección del servidor MySQL
        user='root',       # Usuario de MySQL
        password='contraseña',  # Contraseña de MySQL
        database='BD_Libreria',  # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Funciones CRUD para la tabla Venta
def create_sale(fechaVenta, idUsuario, idEnvio, idArticulo, idPago):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Venta (fechaVenta, Usuario_idUsuario, Envio_idEnvio, Articulo_idArticulo, Pago_idPago)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (fechaVenta, idUsuario, idEnvio, idArticulo, idPago))
        connection.commit()
    finally:
        connection.close()

def read_sales():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Venta")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_sale(idVenta, fechaVenta, idUsuario, idEnvio, idArticulo, idPago):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Venta
            SET fechaVenta=%s, Usuario_idUsuario=%s, Envio_idEnvio=%s, Articulo_idArticulo=%s, Pago_idPago=%s
            WHERE idVenta=%s
            """
            cursor.execute(sql, (fechaVenta, idUsuario, idEnvio, idArticulo, idPago, idVenta))
        connection.commit()
    finally:
        connection.close()

def delete_sale(idVenta):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Venta WHERE idVenta=%s"
            cursor.execute(sql, (idVenta,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Venta
class SaleCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Ventas')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada
        self.fechaVenta_input = QLineEdit(self)
        self.fechaVenta_input.setPlaceholderText('Fecha de Venta (AAAA-MM-DD)')
        layout.addWidget(self.fechaVenta_input)

        # Combo boxes para seleccionar Usuario, Envio, Articulo y Pago
        self.usuario_combo = QComboBox(self)
        self.envio_combo = QComboBox(self)
        self.articulo_combo = QComboBox(self)
        self.pago_combo = QComboBox(self)

        self.populate_comboboxes()

        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel('Usuario:'))
        combo_layout.addWidget(self.usuario_combo)
        layout.addLayout(combo_layout)

        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel('Envío:'))
        combo_layout.addWidget(self.envio_combo)
        layout.addLayout(combo_layout)

        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel('Artículo:'))
        combo_layout.addWidget(self.articulo_combo)
        layout.addLayout(combo_layout)

        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel('Pago:'))
        combo_layout.addWidget(self.pago_combo)
        layout.addLayout(combo_layout)

        # Botones CRUD
        self.create_button = QPushButton('Crear Venta', self)
        self.create_button.clicked.connect(self.create_sale)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Venta', self)
        self.update_button.clicked.connect(self.update_sale)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Venta', self)
        self.delete_button.clicked.connect(self.delete_sale)
        layout.addWidget(self.delete_button)

        # Tabla para mostrar los datos
        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def populate_comboboxes(self):
        # Llenar combo boxes con datos de Usuario, Envio, Articulo y Pago
        self.usuario_combo.clear()
        self.envio_combo.clear()
        self.articulo_combo.clear()
        self.pago_combo.clear()

        # Obtener datos de Usuario, Envio, Articulo y Pago desde la base de datos
        usuarios = read_users()
        envios = read_shipments()
        articulos = read_articles()
        pagos = read_payments()

        for usuario in usuarios:
            self.usuario_combo.addItem(f"{usuario['nombre']} {usuario['apellido']}", usuario['idUsuario'])

        for envio in envios:
            self.envio_combo.addItem(f"ID: {envio['idEnvio']}", envio['idEnvio'])

        for articulo in articulos:
            self.articulo_combo.addItem(f"ID: {articulo['idArticulo']}", articulo['idArticulo'])

        for pago in pagos:
            self.pago_combo.addItem(f"ID: {pago['idPago']}", pago['idPago'])

    def load_data(self):
        sales = read_sales()
        self.table.setRowCount(len(sales))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID Venta', 'Fecha de Venta', 'ID Usuario', 'ID Envío', 'ID Artículo', 'ID Pago'])
        for row_idx, sale in enumerate(sales):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(sale['idVenta'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(sale['fechaVenta'])))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(sale['Usuario_idUsuario'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(sale['Envio_idEnvio'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(sale['Articulo_idArticulo'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(sale['Pago_idPago'])))

    def create_sale(self):
        fechaVenta = self.fechaVenta_input.text()
        idUsuario = self.usuario_combo.currentData()
        idEnvio = self.envio_combo.currentData()
        idArticulo = self.articulo_combo.currentData()
        idPago = self.pago_combo.currentData()

        create_sale(fechaVenta, idUsuario, idEnvio, idArticulo, idPago)
        self.load_data()

    def update_sale(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una venta para actualizar')
            return

        idVenta = int(self.table.item(selected, 0).text())
        fechaVenta = self.fechaVenta_input.text()
        idUsuario = self.usuario_combo.currentData()
        idEnvio = self.envio_combo.currentData()
        idArticulo = self.articulo_combo.currentData()
        idPago = self.pago_combo.currentData()

        update_sale(idVenta, fechaVenta, idUsuario, idEnvio, idArticulo, idPago)
        self.load_data()

    def delete_sale(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una venta para eliminar')
            return

        idVenta = int(self.table.item(selected, 0).text())
        delete_sale(idVenta)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SaleCRUDApp()
    window.show()
    sys.exit(app.exec_())
