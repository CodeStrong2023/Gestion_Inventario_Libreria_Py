from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QIcon, QPixmap
from Frontend.sections.administracionf_ui import Ui_FormADMI
from Frontend.sections.usuarios_ui import Ui_FormUsuarios
from Frontend.sections.ventas_ui import Ui_FormVentas
from Frontend.sections.compras_ui import Ui_FormCompra
#from Frontend.sections.devoluciones_ui import Ui_FormDevoluciones
from Frontend.sections.almacenf_ui import Ui_FormAmacenf
from Frontend.sections.articulos_ui import Ui_FormArt

from Frontend.components.widget import Widget
from Frontend.components.boton import boton
from Frontend.components.tabla import tabla
from Frontend.components.input_text import inputText
from Frontend.components.label import label
from Frontend.components.frame import frame
from Frontend.styles.palette import Palette

class Ui_MainWindow(object):
    def __init__(self, conn):
        self.conn = conn
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.palette = Palette()
        # Establecer el ícono de la ventana
        icon_path = "./assets/icons/favicon.png"  # Reemplaza con la ruta de tu ícono
        icon = QIcon(icon_path)
        MainWindow.setWindowIcon(icon)
        
# Configuración del widget central
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Crear un QVBoxLayout para el centralwidget
        self.central_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        
# Frame para el menú superior
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFixedHeight(51)
        self.frame_2.setStyleSheet("background-color: "+ self.palette.primaryColor+";")
        self.frame_2.setObjectName("frame_2")
        self.central_layout.addWidget(self.frame_2)

        # Layout para el frame_2
        self.frame_2_layout = QtWidgets.QHBoxLayout(self.frame_2)
        self.frame_2_layout.setContentsMargins(10, 10, 10, 10)  # Ajustar márgenes según necesidad
        self.frame_2_layout.setSpacing(20)  # Ajustar espaciado según necesidad

                # Agregar miniatura al lado del label_2
        miniatura_path = icon_path  # Reemplaza con la ruta de tu miniatura
        miniatura_label = QLabel(self.frame_2)
        miniatura_label.setPixmap(QPixmap(miniatura_path).scaledToWidth(40))
        self.frame_2_layout.addWidget(miniatura_label)
        
        # Etiqueta para el nombre de la empresa
        self.label_2 = label().label(self.frame_2, 0, 0, 0, 0, "label_2")
        self.label_2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "color: #C6DCF4")
        self.frame_2_layout.addWidget(self.label_2)
        


        

        self.frame_2_layout.addStretch(1)  # Añadir espacio flexible

        # Botón para el perfil
        #self.boton_perfil = boton().boton(self.frame_2, "background-color:"+self.palette.secondaryColor+"; color:" + self.palette.darkTextColor+"; font-weight: bold; padding: 10px", "Perfil", 0, 0, 75, 23, "BotonPerfil")
        #self.frame_2_layout.addWidget(self.boton_perfil)

        # Botón para salir
        self.boton_salir = boton().boton(self.frame_2, "background-color: rgb(0, 85, 255);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255); padding: 30px;", "Salir", 0, 0, 61, 40, "BottonSalir")
        self.frame_2_layout.addWidget(self.boton_salir)
        # Conectar el botón salir a la función salirApp
        self.boton_salir.clicked.connect(self.salirApp)

        # Crear un QSplitter
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.central_layout.addWidget(self.splitter)

# Frame lateral izquierdo con las opciones
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        self.frame_3.setMinimumWidth(200)
        self.frame_3.setMaximumWidth(200)
        self.frame_3.setStyleSheet("background-color: rgb(52,58,64);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        # Layout para el frame_3
        self.frame_3_layout = QtWidgets.QVBoxLayout(self.frame_3)
        self.frame_3_layout.setContentsMargins(0, 0, 0, 0)

        # Etiqueta para las secciones
        self.section_label = label().label(self.frame_3, 0, 0, 0, 0, "label")
        self.section_label.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "color: #C2C7D0;\n"
                                 "margin-top: 10px;")

        self.section_label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.section_label.setScaledContents(False)
        self.section_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.frame_3_layout.addWidget(self.section_label)

        self.frame_3_layout.addSpacing(20)  # Añadir espaciado

        # Botones para las distintas secciones
        self.administracion = boton().boton(self.frame_3, "color: #C2C7D0", "Administracion", 0, 0, 201, 41, "Administracion")
        self.administracion.setEnabled(True)
        self.administracion.setAutoFillBackground(False)
        self.administracion.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.administracion)

        self.usuarios = boton().boton(self.frame_3, "color: #C2C7D0", "Usuarios", 0, 0, 201, 41, "usuarios")
        self.usuarios.setEnabled(True)
        self.usuarios.setAutoFillBackground(False)
        self.usuarios.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.usuarios)
        
        self.articulo = boton().boton(self.frame_3, "color: #C2C7D0", "Articulos", 0, 0, 201, 41, "Articulos")
        self.articulo.setEnabled(True)
        self.articulo.setAutoFillBackground(False)
        self.articulo.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.articulo)

        self.ventas = boton().boton(self.frame_3, "color: #C2C7D0", "Ventas", 0, 0, 201, 41, "Ventas")
        self.ventas.setEnabled(True)
        self.ventas.setAutoFillBackground(False)
        self.ventas.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.ventas)

        # self.devoluciones = boton().boton(self.frame_3, "color: #C2C7D0", "Devoluciones", 0, 0, 201, 41, "Devoluciones")
        # self.devoluciones.setEnabled(True)
        # self.devoluciones.setAutoFillBackground(False)
        # self.devoluciones.setStyleSheet("color: #C2C7D0")
        # self.frame_3_layout.addWidget(self.devoluciones)

        self.compras = boton().boton(self.frame_3, "color: #C2C7D0", "Compras", 0, 0, 201, 41, "Compras")
        self.compras.setEnabled(True)
        self.compras.setAutoFillBackground(False)
        self.compras.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.compras)

        self.almacen = boton().boton(self.frame_3, "color: #C2C7D0", "Almacen", 0, 0, 201, 41, "Almacen")
        self.almacen.setEnabled(True)
        self.almacen.setAutoFillBackground(False)
        self.almacen.setStyleSheet("color: #C2C7D0")
        self.frame_3_layout.addWidget(self.almacen)

        self.frame_3_layout.addStretch(1)  # Añadir espacio flexible al final

        # Frame para las páginas principales
        self.pages_frame = QtWidgets.QFrame(self.splitter)
        self.pages_frame.setStyleSheet("background-color: pink;")
        self.pages_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pages_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pages_frame.setObjectName("pages_frame")

        # Layout para el pages_frame
        self.pages_frame_layout = QtWidgets.QVBoxLayout(self.pages_frame)
        self.pages_frame_layout.setContentsMargins(0, 0, 0, 0)

        # Stacked widget para manejar las páginas
        self.stacked_widget_pages = QtWidgets.QStackedWidget(self.pages_frame)
        self.stacked_widget_pages.setObjectName("stackedWidget")
        self.pages_frame_layout.addWidget(self.stacked_widget_pages)

        # Página 1 (administracion)
        

        
        self.page_1 = QtWidgets.QWidget()
        self.Ui_FormAdministracion = Ui_FormADMI(self.conn)
        self.Ui_FormAdministracion.setupUi(self.page_1, self.palette)
        self.stacked_widget_pages.addWidget(self.page_1)

        # Página 2 (usuarios)
        self.page_2 = QtWidgets.QWidget()
        self.Ui_FormUsuarios = Ui_FormUsuarios(self.conn)
        self.Ui_FormUsuarios.setupUi(self.page_2, self.palette)
        self.stacked_widget_pages.addWidget(self.page_2)
        
        #Pagina 3 (articulos)
        self.page_3 = QtWidgets.QWidget()
        self.Ui_FormArticulos = Ui_FormArt(self.conn)
        self.Ui_FormArticulos.setupUi(self.page_3, self.palette)
        self.stacked_widget_pages.addWidget(self.page_3)
        
        # Página 4 (ventas)
        self.page_4 = QtWidgets.QWidget()
        self.Ui_FormVentas = Ui_FormVentas(self.conn)
        self.Ui_FormVentas.setupUi(self.page_4, self.palette)
        self.stacked_widget_pages.addWidget(self.page_4)
        
        # Página 5 (compras)
        self.page_5 = QtWidgets.QWidget()
        self.Ui_FormCompra = Ui_FormCompra(self.conn)
        self.Ui_FormCompra.setupUi(self.page_5, self.palette)
        self.stacked_widget_pages.addWidget(self.page_5)
        
        # # Página 6 (devoluciones)
        # self.page_6 = QtWidgets.QWidget()
        # self.Ui_FormDevoluciones = Ui_FormDevoluciones(self.conn)
        # self.Ui_FormDevoluciones.setupUi(self.page_6, self.palette)
        # self.stacked_widget_pages.addWidget(self.page_6)
        
        # Página 6 (almacen)
        self.page_6 = QtWidgets.QWidget()
        self.Ui_FormAlmacen = Ui_FormAmacenf(self.conn)
        self.Ui_FormAlmacen.setupUi(self.page_6, self.palette)
        self.stacked_widget_pages.addWidget(self.page_6)

        # Configuración del widget central de la ventana principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Conexión de señales y slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Conectar botones a funciones
        self.administracion.clicked.connect(self.showAdministracion)
        self.usuarios.clicked.connect(self.showUsuarios)
        self.ventas.clicked.connect(self.showVentas)
        self.compras.clicked.connect(self.showCompras)
        # self.devoluciones.clicked.connect(self.showDevoluciones)
        self.almacen.clicked.connect(self.showAlmacen)
        self.articulo.clicked.connect(self.showArticulos)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestor de Librería"))
        self.boton_salir.setText(_translate("MainWindow", "Salir"))
        #self.boton_perfil.setText(_translate("MainWindow", "Perfil"))
        self.label_2.setText(_translate("MainWindow", "GESTOR DE LIBRERIA"))
        self.section_label.setText(_translate("MainWindow", "SECCIONES"))
        
        self.administracion.setText(_translate("MainWindow", "Administracion"))
        self.usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.ventas.setText(_translate("MainWindow", "Ventas"))
        # self.devoluciones.setText(_translate("MainWindow", "Devoluciones"))
        self.compras.setText(_translate("MainWindow", "Compras"))
        self.almacen.setText(_translate("MainWindow", "Almacen"))
        
    def showAdministracion(self):
        self.stacked_widget_pages.setCurrentIndex(0)
    
    def showUsuarios(self):
        self.stacked_widget_pages.setCurrentIndex(1)
        
    def showArticulos(self):
        self.stacked_widget_pages.setCurrentIndex(2)
        
    def showVentas(self):
        self.stacked_widget_pages.setCurrentIndex(3)
        
    def showCompras(self):
        self.stacked_widget_pages.setCurrentIndex(4)
        
    # def showDevoluciones(self):
    #     self.stacked_widget_pages.setCurrentIndex(7)
    
    def showAlmacen(self):
        self.stacked_widget_pages.setCurrentIndex(5)
        
    def salirApp(self):
        QtWidgets.QApplication.instance().quit()