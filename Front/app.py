import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Layoud_ui import Ui_MainWindow

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        # Instancia el objeto de la interfaz gráfica
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Configura la interfaz en la ventana principal

        # Puedes conectar señales y slots aquí si es necesario

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
