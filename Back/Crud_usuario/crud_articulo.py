from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox
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

# Funciones CRUD para la tabla Articulo
def create_article(alto, ancho, peso, precio, tipo):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            INSERT INTO Articulo (alto, ancho, peso, precio, tipo)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (alto, ancho, peso, precio, tipo))
        connection.commit()
    finally:
        connection.close()

def read_articles():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Articulo")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_article(id_articulo, alto, ancho, peso, precio, tipo):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            UPDATE Articulo
            SET alto=%s, ancho=%s, peso=%s, precio=%s, tipo=%s
            WHERE idArticulo=%s
            """
            cursor.execute(sql, (alto, ancho, peso, precio, tipo, id_articulo))
        connection.commit()
    finally:
        connection.close()

def delete_article(id_articulo):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM Articulo WHERE idArticulo=%s"
            cursor.execute(sql, (id_articulo,))
        connection.commit()
    finally:
        connection.close()

# Aplicación PyQt5 para el CRUD de Articulo
class ArticleCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Artículos')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada
        self.alto_input = QLineEdit(self)
        self.alto_input.setPlaceholderText('Alto')
        layout.addWidget(self.alto_input)

        self.ancho_input = QLineEdit(self)
        self.ancho_input.setPlaceholderText('Ancho')
        layout.addWidget(self.ancho_input)

        self.peso_input = QLineEdit(self)
        self.peso_input.setPlaceholderText('Peso')
        layout.addWidget(self.peso_input)

        self.precio_input = QLineEdit(self)
        self.precio_input.setPlaceholderText('Precio')
        layout.addWidget(self.precio_input)

        self.tipo_input = QLineEdit(self)
        self.tipo_input.setPlaceholderText('Tipo')
        layout.addWidget(self.tipo_input)

        # Botones CRUD
        self.create_button = QPushButton('Crear Artículo', self)
        self.create_button.clicked.connect(self.create_article)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Artículo', self)
        self.update_button.clicked.connect(self.update_article)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Artículo', self)
        self.delete_button.clicked.connect(self.delete_article)
        layout.addWidget(self.delete_button)

        # Tabla para mostrar los datos
        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        articles = read_articles()
        self.table.setRowCount(len(articles))
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Alto', 'Ancho', 'Peso', 'Precio', 'Tipo'])
        for row_idx, article in enumerate(articles):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(article['idArticulo'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(article['alto']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(article['ancho']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(article['peso']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(article['precio'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(article['tipo']))

    def create_article(self):
        alto = self.alto_input.text()
        ancho = self.ancho_input.text()
        peso = self.peso_input.text()
        precio = float(self.precio_input.text())
        tipo = self.tipo_input.text()

        create_article(alto, ancho, peso, precio, tipo)
        self.load_data()

    def update_article(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un artículo para actualizar')
            return

        id_articulo = int(self.table.item(selected, 0).text())
        alto = self.alto_input.text()
        ancho = self.ancho_input.text()
        peso = self.peso_input.text()
        precio = float(self.precio_input.text())
        tipo = self.tipo_input.text()

        update_article(id_articulo, alto, ancho, peso, precio, tipo)
        self.load_data()

    def delete_article(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un artículo para eliminar')
            return

        id_articulo = int(self.table.item(selected, 0).text())
        delete_article(id_articulo)
        self.load_data()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArticleCRUDApp()
    window.show()
    sys.exit(app.exec_())
