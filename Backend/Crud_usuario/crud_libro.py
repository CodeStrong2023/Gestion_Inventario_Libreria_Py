from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox, QComboBox, QFileDialog
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

# Funciones CRUD para Libro
def create_libro(titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO `BD_Libreria`.`Libro` 
                     (titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, Articulo_idArticulo, genero_idgenero, Editorial_idEditorial) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id))
        connection.commit()
    finally:
        connection.close()

def read_libros():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM `BD_Libreria`.`Libro`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def update_libro(id_libro, titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """UPDATE `BD_Libreria`.`Libro` 
                     SET titulo=%s, idioma=%s, tapa=%s, año=%s, isbn=%s, paginas=%s, edicion=%s, edad_minima=%s, edad_maxima=%s, descripcion=%s, imagen_tapa=%s, Articulo_idArticulo=%s, genero_idgenero=%s, Editorial_idEditorial=%s 
                     WHERE idLibro=%s"""
            cursor.execute(sql, (titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id, id_libro))
        connection.commit()
    finally:
        connection.close()

def delete_libro(id_libro):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `BD_Libreria`.`Libro` WHERE idLibro=%s"
            cursor.execute(sql, (id_libro,))
        connection.commit()
    finally:
        connection.close()

def read_articles():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idArticulo, tipo FROM `BD_Libreria`.`Articulo`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def read_genres():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idgenero, nombre FROM `BD_Libreria`.`genero`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

def read_editorials():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idEditorial, nombre FROM `BD_Libreria`.`Editorial`")
            result = cursor.fetchall()
            return result
    finally:
        connection.close()

# Aplicación PyQt5 para CRUD de Libro
class LibroCRUDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('CRUD de Libro')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Campos de entrada y botones
        self.titulo_input = QLineEdit(self)
        self.titulo_input.setPlaceholderText('Título')
        layout.addWidget(self.titulo_input)

        self.idioma_input = QLineEdit(self)
        self.idioma_input.setPlaceholderText('Idioma')
        layout.addWidget(self.idioma_input)

        self.tapa_input = QLineEdit(self)
        self.tapa_input.setPlaceholderText('Tapa')
        layout.addWidget(self.tapa_input)

        self.año_input = QLineEdit(self)
        self.año_input.setPlaceholderText('Año')
        layout.addWidget(self.año_input)

        self.isbn_input = QLineEdit(self)
        self.isbn_input.setPlaceholderText('ISBN')
        layout.addWidget(self.isbn_input)

        self.paginas_input = QLineEdit(self)
        self.paginas_input.setPlaceholderText('Páginas')
        layout.addWidget(self.paginas_input)

        self.edicion_input = QLineEdit(self)
        self.edicion_input.setPlaceholderText('Edición')
        layout.addWidget(self.edicion_input)

        self.edad_minima_input = QLineEdit(self)
        self.edad_minima_input.setPlaceholderText('Edad Mínima')
        layout.addWidget(self.edad_minima_input)

        self.edad_maxima_input = QLineEdit(self)
        self.edad_maxima_input.setPlaceholderText('Edad Máxima')
        layout.addWidget(self.edad_maxima_input)

        self.descripcion_input = QLineEdit(self)
        self.descripcion_input.setPlaceholderText('Descripción')
        layout.addWidget(self.descripcion_input)

        self.imagen_tapa_input = QLineEdit(self)
        self.imagen_tapa_input.setPlaceholderText('Ruta de la Imagen de la Tapa')
        layout.addWidget(self.imagen_tapa_input)

        self.browse_button = QPushButton('Buscar Imagen de Tapa', self)
        self.browse_button.clicked.connect(self.browse_image)
        layout.addWidget(self.browse_button)

        self.articulo_combo = QComboBox(self)
        self.load_articulos()
        layout.addWidget(self.articulo_combo)

        self.genero_combo = QComboBox(self)
        self.load_generos()
        layout.addWidget(self.genero_combo)

        self.editorial_combo = QComboBox(self)
        self.load_editoriales()
        layout.addWidget(self.editorial_combo)

        self.create_button = QPushButton('Crear Libro', self)
        self.create_button.clicked.connect(self.create_libro)
        layout.addWidget(self.create_button)

        self.update_button = QPushButton('Actualizar Libro', self)
        self.update_button.clicked.connect(self.update_libro)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Eliminar Libro', self)
        self.delete_button.clicked.connect(self.delete_libro)
        layout.addWidget(self.delete_button)

        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        libros = read_libros()
        self.table.setRowCount(len(libros))
        self.table.setColumnCount(14)
        self.table.setHorizontalHeaderLabels(['ID', 'Título', 'Idioma', 'Tapa', 'Año', 'ISBN', 'Páginas', 'Edición', 'Edad Mínima', 'Edad Máxima', 'Descripción', 'Imagen Tapa', 'ID Artículo', 'ID Género', 'ID Editorial'])
        for row_idx, libro in enumerate(libros):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(libro['idLibro'])))
            self.table.setItem(row_idx, 1, QTableWidgetItem(libro['titulo']))
            self.table.setItem(row_idx, 2, QTableWidgetItem(libro['idioma']))
            self.table.setItem(row_idx, 3, QTableWidgetItem(libro['tapa']))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(libro['año'])))
            self.table.setItem(row_idx, 5, QTableWidgetItem(libro['isbn']))
            self.table.setItem(row_idx, 6, QTableWidgetItem(libro['paginas']))
            self.table.setItem(row_idx, 7, QTableWidgetItem(libro['edicion']))
            self.table.setItem(row_idx, 8, QTableWidgetItem(str(libro['edad_minima'])))
            self.table.setItem(row_idx, 9, QTableWidgetItem(str(libro['edad_maxima'])))
            self.table.setItem(row_idx, 10, QTableWidgetItem(libro['descripcion']))
            self.table.setItem(row_idx, 11, QTableWidgetItem(libro['imagen_tapa']))
            self.table.setItem(row_idx, 12, QTableWidgetItem(str(libro['Articulo_idArticulo'])))
            self.table.setItem(row_idx, 13, QTableWidgetItem(str(libro['genero_idgenero'])))
            self.table.setItem(row_idx, 14, QTableWidgetItem(str(libro['Editorial_idEditorial'])))

    def browse_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Imagen de Tapa", "", "Imagenes (*.png *.xpm *.jpg *.jpeg);;Todos los archivos (*)", options=options)
        if file_path:
            self.imagen_tapa_input.setText(file_path)

    def load_articulos(self):
        articulos = read_articles()
        for articulo in articulos:
            self.articulo_combo.addItem(articulo['tipo'], articulo['idArticulo'])

    def load_generos(self):
        generos = read_genres()
        for genero in generos:
            self.genero_combo.addItem(genero['nombre'], genero['idgenero'])

    def load_editoriales(self):
        editoriales = read_editorials()
        for editorial in editoriales:
            self.editorial_combo.addItem(editorial['nombre'], editorial['idEditorial'])

    def create_libro(self):
        titulo = self.titulo_input.text()
        idioma = self.idioma_input.text()
        tapa = self.tapa_input.text()
        año = int(self.año_input.text()) if self.año_input.text().isdigit() else None
        isbn = self.isbn_input.text()
        paginas = self.paginas_input.text()
        edicion = self.edicion_input.text()
        edad_minima = int(self.edad_minima_input.text()) if self.edad_minima_input.text().isdigit() else None
        edad_maxima = int(self.edad_maxima_input.text()) if self.edad_maxima_input.text().isdigit() else None
        descripcion = self.descripcion_input.text()
        imagen_tapa = self.imagen_tapa_input.text()
        articulo_id = self.articulo_combo.currentData()
        genero_id = self.genero_combo.currentData()
        editorial_id = self.editorial_combo.currentData()

        if not titulo or not idioma or not tapa or not articulo_id or not genero_id or not editorial_id:
            QMessageBox.warning(self, 'Error', 'Los campos "Título", "Idioma", "Tapa", "Artículo", "Género" y "Editorial" no pueden estar vacíos')
            return

        create_libro(titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id)
        self.load_data()
        self.clear_inputs()

    def update_libro(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un libro para actualizar')
            return

        id_libro = int(self.table.item(selected, 0).text())
        titulo = self.titulo_input.text()
        idioma = self.idioma_input.text()
        tapa = self.tapa_input.text()
        año = int(self.año_input.text()) if self.año_input.text().isdigit() else None
        isbn = self.isbn_input.text()
        paginas = self.paginas_input.text()
        edicion = self.edicion_input.text()
        edad_minima = int(self.edad_minima_input.text()) if self.edad_minima_input.text().isdigit() else None
        edad_maxima = int(self.edad_maxima_input.text()) if self.edad_maxima_input.text().isdigit() else None
        descripcion = self.descripcion_input.text()
        imagen_tapa = self.imagen_tapa_input.text()
        articulo_id = self.articulo_combo.currentData()
        genero_id = self.genero_combo.currentData()
        editorial_id = self.editorial_combo.currentData()

        if not titulo or not idioma or not tapa or not articulo_id or not genero_id or not editorial_id:
            QMessageBox.warning(self, 'Error', 'Los campos "Título", "Idioma", "Tapa", "Artículo", "Género" y "Editorial" no pueden estar vacíos')
            return

        update_libro(id_libro, titulo, idioma, tapa, año, isbn, paginas, edicion, edad_minima, edad_maxima, descripcion, imagen_tapa, articulo_id, genero_id, editorial_id)
        self.load_data()
        self.clear_inputs()

    def delete_libro(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, 'Error', 'Selecciona un libro para eliminar')
            return

        id_libro = int(self.table.item(selected, 0).text())
        delete_libro(id_libro)
        self.load_data()
        self.clear_inputs()

    def clear_inputs(self):
        self.titulo_input.clear()
        self.idioma_input.clear()
        self.tapa_input.clear()
        self.año_input.clear()
        self.isbn_input.clear()
        self.paginas_input.clear()
        self.edicion_input.clear()
        self.edad_minima_input.clear()
        self.edad_maxima_input.clear()
        self.descripcion_input.clear()
        self.imagen_tapa_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibroCRUDApp()
    window.show()
    sys.exit(app.exec_())
