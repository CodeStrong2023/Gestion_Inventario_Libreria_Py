import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Frontend.layout_ui import Ui_MainWindow
from Backend.database.connection import Connection

def main():
    conn = Connection().abrirConexion()
    return conn

class MiVentana(QMainWindow):
    def __init__(self, conn):
        super().__init__()
        self.ui = Ui_MainWindow(conn) 
        self.conn = conn
        self.ui.setupUi(self)
        self.showMaximized()

    def apply_palette(self):
        # Obtener la paleta desde la instancia de Palette
        app_palette = self.palette.get_palette()

        # Aplicar la paleta a la ventana principal
        self.setPalette(app_palette)

        # Aplicar la paleta a los widgets específicos
        self.ui.label_2.setPalette(app_palette)  # Ejemplo de aplicar a un QLabel
        self.ui.boton_salir.setPalette(app_palette)  # Ejemplo de aplicar a un QPushButton
        # Añadir más widgets según sea necesario

    def resizeEvent(self, event):
        self.ui.pages_frame.setGeometry(200, 50, self.width() - 200, self.height() - 50)
        self.ui.stacked_widget_pages.setGeometry(0, 0, self.ui.pages_frame.width(), self.ui.pages_frame.height())
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    conn = main()
    ventana = MiVentana(conn)
    ventana.show()
    sys.exit(app.exec())
