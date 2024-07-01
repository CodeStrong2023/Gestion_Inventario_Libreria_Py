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

# Función para cargar autores desde la base de datos
def read_autores():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idAutor, nombre FROM Autor")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Función para cargar libros desde la base de datos
def read_libros():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idLibro, titulo FROM Libro")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Clase principal para la aplicación CRUD de Autor_has_Libro
class AutorLibroCRUDApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CRUD de Autor_has_Libro')
        self.setGeometry(200, 200, 500, 400)
        self.initUI()

    def initUI(self):
        # Widgets
        self.label_autor = QLabel('Autor:')
        self.combo_autor = QComboBox()
        self.load_autores()

        self.label_libro = QLabel('Libro:')
        self.combo_libro = QComboBox()
        self.load_libros()

        self.btn_guardar = QPushButton('Guardar')
        self.btn_guardar.clicked.connect(self.guardar_autor_libro)

        self.btn_eliminar = QPushButton('Eliminar')
        self.btn_eliminar.clicked.connect(self.eliminar_autor_libro)

        # Layout
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow(self.label_autor, self.combo_autor)
        form_layout.addRow(self.label_libro, self.combo_libro)
        layout.addLayout(form_layout)
        layout.addWidget(self.btn_guardar)
        layout.addWidget(self.btn_eliminar)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_autores(self):
        autores = read_autores()
        for autor in autores:
            self.combo_autor.addItem(f"{autor['idAutor']} - {autor['nombre']}")

    def load_libros(self):
        libros = read_libros()
        for libro in libros:
            self.combo_libro.addItem(f"{libro['idLibro']} - {libro['titulo']}")

    def guardar_autor_libro(self):
        id_autor = int(self.combo_autor.currentText().split()[0])
        id_libro = int(self.combo_libro.currentText().split()[0])

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO Autor_has_Libro (Autor_idAutor, Libro_idLibro, Libro_Articulo_idArticulo) VALUES (%s, %s, %s)"
                cursor.execute(sql, (id_autor, id_libro, id_libro))
                connection.commit()
                QMessageBox.information(self, 'Éxito', 'Relación Autor-Libro guardada correctamente.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al guardar la Relación Autor-Libro:\n{str(e)}')
        finally:
            connection.close()

    def eliminar_autor_libro(self):
        id_autor = int(self.combo_autor.currentText().split()[0])
        id_libro = int(self.combo_libro.currentText().split()[0])

        if not id_autor or not id_libro:
            QMessageBox.warning(self, 'Advertencia', 'Selecciona un Autor y un Libro para eliminar la relación.')
            return

        confirmacion = QMessageBox.question(self, 'Confirmar Eliminación', '¿Estás seguro de eliminar esta Relación Autor-Libro?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirmacion == QMessageBox.Yes:
            connection = get_db_connection()
            try:
                with connection.cursor() as cursor:
                    sql = "DELETE FROM Autor_has_Libro WHERE Autor_idAutor=%s AND Libro_idLibro=%s"
                    cursor.execute(sql, (id_autor, id_libro))
                    connection.commit()
                    QMessageBox.information(self, 'Éxito', 'Relación Autor-Libro eliminada correctamente.')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al eliminar la Relación Autor-Libro:\n{str(e)}')
            finally:
                connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutorLibroCRUDApp()
    window.show()
    sys.exit(app.exec_())
