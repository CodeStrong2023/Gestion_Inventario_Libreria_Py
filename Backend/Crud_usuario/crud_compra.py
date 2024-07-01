from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox, QComboBox, QDateEdit
import sys
import pymysql
from PyQt5.QtCore import QDate

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',    # Dirección del servidor MySQL
        user='root',         # Usuario de MySQL
        password='contraseña',  # Contraseña de MySQL
        database='BD_Libreria',    # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Funciones CRUD para Compra
def create_compra(almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO `BD_Libreria`.`Compra` 
                     (Almacenamiento_idAlmacenamiento, Articulo_idArticulo, fecha, cantidad, precioUnitario, Pago_idPago, Proveedor_idProveedor) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id))
        connection.commit()
    finally:
        connection.close()

def read_compras():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Compra`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_compra(compra_id, almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """UPDATE `BD_Libreria`.`Compra` 
                     SET Almacenamiento_idAlmacenamiento=%s, Articulo_idArticulo=%s, fecha=%s, cantidad=%s, precioUnitario=%s, Pago_idPago=%s, Proveedor_idProveedor=%s 
                     WHERE CompraId=%s"""
            cursor.execute(sql, (almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id, compra_id))
        connection.commit()
    finally:
        connection.close()

def delete_compra(compra_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Compra` WHERE CompraId=%s"
            cursor.execute(sql, (compra_id,))
        connection.commit()
    finally:
        connection.close()

# Funciones para leer datos relacionados
def read_almacenamientos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idAlmacenamiento, usoM3 FROM `BD_Libreria`.`Almacenamiento`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def read_articulos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idArticulo, tipo FROM `BD_Libreria`.`Articulo`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def read_pagos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idPago, tipo FROM `BD_Libreria`.`Pago`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def read_proveedores():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idProveedor, nombre FROM `BD_Libreria`.`Proveedor`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Compra
class CompraCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Compra')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.fecha_input = QDateEdit(self)
        self.fecha_input.setCalendarPopup(True)
        self.fecha_input.setDisplayFormat('yyyy-MM-dd')
        layout.addWidget(self.fecha_input)

        self.cantidad_input = QLineEdit(self)
        self.cantidad_input.setPlaceholderText('Cantidad')
        layout.addWidget(self.cantidad_input)

        self.precio_unitario_input = QLineEdit(self)
        self.precio_unitario_input.setPlaceholderText('Precio Unitario')
        layout.addWidget(self.precio_unitario_input)

        self.almacenamiento_combo = QComboBox(self)
        self.load_almacenamientos()
        layout.addWidget(self.almacenamiento_combo)

        self.articulo_combo = QComboBox(self)
        self.load_articulos()
        layout.addWidget(self.articulo_combo)

        self.pago_combo = QComboBox(self)
        self.load_pagos()
        layout.addWidget(self.pago_combo)

        self.proveedor_combo = QComboBox(self)
        self.load_proveedores()
        layout.addWidget(self.proveedor_combo)

        self.create_button = QPushButton('Crear Compra', self)
        self.create_button.clicked.connect(self.create_compra)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Compra', self)
        self.update_button.clicked.connect(self.update_compra)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Compra', self)
        self.delete_button.clicked.connect(self.delete_compra)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        compras = read_compras()
        self.table.setRowCount(len(compras))
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(['ID Compra', 'ID Almacenamiento', 'ID Artículo', 'Fecha', 'Cantidad', 'Precio Unitario', 'ID Pago', 'ID Proveedor'])
        for row_idx, compra in enumerate(compras):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(compra['CompraId'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(compra['Almacenamiento_idAlmacenamiento'])))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(compra['Articulo_idArticulo'])))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(compra['fecha'])))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(compra['cantidad'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(compra['precioUnitario'])))
            self.table.setItem(row_idx, 6, QTableWidgetItem(str(compra['Pago_idPago'])))
            self.table.setItem(row_idx, 7, QTableWidgetItem(str(compra['Proveedor_idProveedor'])))

    def load_almacenamientos(self):
        almacenamientos = read_almacenamientos()
        for almacenamiento in almacenamientos:
            self.almacenamiento_combo.addItem(almacenamiento['usoM3'], almacenamiento['idAlmacenamiento'])

    def load_articulos(self):
        articulos = read_articulos()
        for articulo in articulos:
            self.articulo_combo.addItem(articulo['tipo'], articulo['idArticulo'])

    def load_pagos(self):
        pagos = read_pagos()
        for pago in pagos:
            self.pago_combo.addItem(str(pago['tipo']), pago['idPago'])

    def load_proveedores(self):
        proveedores = read_proveedores()
        for proveedor in proveedores:
            self.proveedor_combo.addItem(proveedor['nombre'], proveedor['idProveedor'])

    def create_compra(self):
        almacenamiento_id = self.almacenamiento_combo.currentData()
        articulo_id = self.articulo_combo.currentData()
        fecha = self.fecha_input.date().toString('yyyy-MM-dd')
        cantidad = int(self.cantidad_input.text()) if self.cantidad_input.text().isdigit() else None
        precio_unitario = float(self.precio_unitario_input.text()) if self.precio_unitario_input.text() else None
        pago_id = self.pago_combo.currentData()
        proveedor_id = self.proveedor_combo.currentData()

        if not almacenamiento_id or not articulo_id or not pago_id or not proveedor_id:
            QMessageBox.warning(self, 'Error', 'Los campos "Almacenamiento", "Artículo", "Pago" y "Proveedor" no pueden estar vacíos')
            return

        create_compra(almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id)
        self.load_data()
        self.clear_inputs()

    def update_compra(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una compra para actualizar')
            return

        compra_id = int(self.table.item(selected, 0).text())
        almacenamiento_id = self.almacenamiento_combo.currentData()
        articulo_id = self.articulo_combo.currentData()
        fecha = self.fecha_input.date().toString('yyyy-MM-dd')
        cantidad = int(self.cantidad_input.text()) if self.cantidad_input.text().isdigit() else None
        precio_unitario = float(self.precio_unitario_input.text()) if self.precio_unitario_input.text() else None
        pago_id = self.pago_combo.currentData()
        proveedor_id = self.proveedor_combo.currentData()

        if not almacenamiento_id or not articulo_id or not pago_id or not proveedor_id:
            QMessageBox.warning(self, 'Error', 'Los campos "Almacenamiento", "Artículo", "Pago" y "Proveedor" no pueden estar vacíos')
            return

        update_compra(compra_id, almacenamiento_id, articulo_id, fecha, cantidad, precio_unitario, pago_id, proveedor_id)
        self.load_data()
        self.clear_inputs()

    def delete_compra(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona una compra para eliminar')
            return

        compra_id = int(self.table.item(selected, 0).text())
        delete_compra(compra_id)
        self.load_data()
        self.clear_inputs()

    def clear_inputs(self):
        self.fecha_input.setDate(QDate.currentDate())
        self.cantidad_input.clear()
        self.precio_unitario_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CompraCRUDApp()
    window.show()
    sys.exit(app.exec_())
