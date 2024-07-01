import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout, QComboBox, QMessageBox
import pymysql.cursors

# Función para conectar a la base de datos
def get_db_connection():
    return pymysql.connect(
        host='127.0.0.1',    # Dirección del servidor MySQL
        user='root',         # Usuario de MySQL
        password='contraseña',  # Contraseña de MySQL
        database='BD_Libreria',    # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Para obtener resultados como diccionarios
    )

# Función para cargar artículos desde la base de datos
def read_articulos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idArticulo, tipo FROM Articulo")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Función para cargar editoriales desde la base de datos
def read_editoriales():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idEditorial, nombre FROM Editorial")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Función para cargar géneros desde la base de datos
def read_generos():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idgenero, nombre FROM genero")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Clase principal para la aplicación CRUD de Revista
class RevistaCRUDApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CRUD de Revista')
        self.setGeometry(200, 200, 500, 400)
        self.initUI()

    def initUI(self):
        # Widgets
        self.label_titulo = QLabel('Título:')
        self.input_titulo = QLineEdit()

        self.label_numero = QLabel('Número:')
        self.input_numero = QLineEdit()

        self.label_anio = QLabel('Año:')
        self.input_anio = QLineEdit()

        self.label_mes = QLabel('Mes:')
        self.input_mes = QLineEdit()

        self.label_dia = QLabel('Día:')
        self.input_dia = QLineEdit()

        self.label_articulo = QLabel('Artículo:')
        self.combo_articulo = QComboBox()
        self.load_articulos()

        self.label_editorial = QLabel('Editorial:')
        self.combo_editorial = QComboBox()
        self.load_editoriales()

        self.label_genero = QLabel('Género:')
        self.combo_genero = QComboBox()
        self.load_generos()

        self.btn_guardar = QPushButton('Guardar')
        self.btn_guardar.clicked.connect(self.guardar_revista)

        self.btn_actualizar = QPushButton('Actualizar')
        self.btn_actualizar.clicked.connect(self.actualizar_revista)

        self.btn_eliminar = QPushButton('Eliminar')
        self.btn_eliminar.clicked.connect(self.eliminar_revista)

        self.btn_limpiar = QPushButton('Limpiar')
        self.btn_limpiar.clicked.connect(self.limpiar_campos)

        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow(self.label_titulo, self.input_titulo)
        form_layout.addRow(self.label_numero, self.input_numero)
        form_layout.addRow(self.label_anio, self.input_anio)
        form_layout.addRow(self.label_mes, self.input_mes)
        form_layout.addRow(self.label_dia, self.input_dia)
        form_layout.addRow(self.label_articulo, self.combo_articulo)
        form_layout.addRow(self.label_editorial, self.combo_editorial)
        form_layout.addRow(self.label_genero, self.combo_genero)
        layout.addLayout(form_layout)
        layout.addWidget(self.btn_guardar)
        layout.addWidget(self.btn_actualizar)
        layout.addWidget(self.btn_eliminar)
        layout.addWidget(self.btn_limpiar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_articulos(self):
        articulos = read_articulos()
        for articulo in articulos:
            self.combo_articulo.addItem(f"{articulo['idArticulo']} - {articulo['tipo']}")

    def load_editoriales(self):
        editoriales = read_editoriales()
        for editorial in editoriales:
            self.combo_editorial.addItem(f"{editorial['idEditorial']} - {editorial['nombre']}")

    def load_generos(self):
        generos = read_generos()
        for genero in generos:
            self.combo_genero.addItem(f"{genero['idgenero']} - {genero['nombre']}")

    def guardar_revista(self):
        titulo = self.input_titulo.text()
        numero = self.input_numero.text()
        anio = self.input_anio.text()
        mes = self.input_mes.text()
        dia = self.input_dia.text()
        id_articulo = int(self.combo_articulo.currentText().split()[0])
        id_editorial = int(self.combo_editorial.currentText().split()[0])
        id_genero = int(self.combo_genero.currentText().split()[0])

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Revista (titulo, numero, anio, mes, dia, Articulo_idArticulo, Editorial_idEditorial, genero_idgenero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (titulo, numero, anio, mes, dia, id_articulo, id_editorial, id_genero))
                connection.commit()
                QMessageBox.information(self, 'Éxito', 'Revista guardada correctamente.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al guardar la Revista:\n{str(e)}')
        finally:
            connection.close()
            self.limpiar_campos()

    def actualizar_revista(self):
        titulo = self.input_titulo.text()
        numero = self.input_numero.text()
        anio = self.input_anio.text()
        mes = self.input_mes.text()
        dia = self.input_dia.text()
        id_articulo = int(self.combo_articulo.currentText().split()[0])
        id_editorial = int(self.combo_editorial.currentText().split()[0])
        id_genero = int(self.combo_genero.currentText().split()[0])

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE Revista SET titulo=%s, numero=%s, anio=%s, mes=%s, dia=%s, Editorial_idEditorial=%s, genero_idgenero=%s WHERE Articulo_idArticulo=%s"
                cursor.execute(sql, (titulo, numero, anio, mes, dia, id_editorial, id_genero, id_articulo))
                connection.commit()
                QMessageBox.information(self, 'Éxito', 'Revista actualizada correctamente.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al actualizar la Revista:\n{str(e)}')
        finally:
            connection.close()
            self.limpiar_campos()

    def eliminar_revista(self):
        id_articulo = int(self.combo_articulo.currentText().split()[0])

        if not id_articulo:
            QMessageBox.warning(self, 'Advertencia', 'Selecciona una Revista para eliminar.')
            return

        confirmacion = QMessageBox.question(self, 'Confirmar Eliminación', '¿Estás seguro de eliminar esta Revista?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmacion == QMessageBox.Yes:
            connection = get_db_connection()
            try:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM Revista WHERE Articulo_idArticulo=%s"
                    cursor.execute(sql, (id_articulo,))
                    connection.commit()
                    QMessageBox.information(self, 'Éxito', 'Revista eliminada correctamente.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al eliminar la Revista:\n{str(e)}')
            finally:
                connection.close()
                self.limpiar_campos()

    def limpiar_campos(self):
        self.input_titulo.setText('')
        self.input_numero.setText('')
        self.input_anio.setText('')
        self.input_mes.setText('')
        self.input_dia.setText('')
        self.combo_articulo.setCurrentIndex(0)
        self.combo_editorial.setCurrentIndex(0)
        self.combo_genero.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RevistaCRUDApp()
    window.show()
    sys.exit(app.exec_())
