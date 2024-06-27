

from PyQt6 import QtCore, QtGui, QtWidgets
from Secciones.administracionf_ui import Ui_FormADMI
from Secciones.usuarios_ui import Ui_FormUsuarios
from Secciones.ventas_ui import Ui_FormVentas
from Secciones.compras_ui import Ui_FormCompra 
from Secciones.devoluciones_ui import Ui_FormDevoluciones
from Secciones.almacenf_ui import Ui_FormAmacenf

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Configuración de la ventana principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 840)

        # Configuración del widget central
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Frame para el nombre de la empresa
        self.NameEmpresa = QtWidgets.QFrame(parent=self.centralwidget)
        self.NameEmpresa.setGeometry(QtCore.QRect(0, 0, 1101, 841))
        self.NameEmpresa.setStyleSheet("background-color: rgb(246, 244, 249);")
        self.NameEmpresa.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.NameEmpresa.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.NameEmpresa.setObjectName("NameEmpresa")

        # Frame superior dentro del frame NameEmpresa
        self.frame_2 = QtWidgets.QFrame(parent=self.NameEmpresa)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1201, 51))
        self.frame_2.setStyleSheet("background-color: rgb(17, 130, 249);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        # Botón para salir
        self.BottonSalir = QtWidgets.QPushButton(parent=self.frame_2)
        self.BottonSalir.setGeometry(QtCore.QRect(1030, 10, 61, 23))
        self.BottonSalir.setStyleSheet("background-color: rgb(0, 85, 255);\n"
                                        "font: 14pt \"MS Shell Dlg 2\";\n"
                                        "color:rgb(255, 255, 255)")
        self.BottonSalir.setObjectName("BottonSalir")

        # Botón para el perfil
        self.BotonPerfil = QtWidgets.QPushButton(parent=self.frame_2)
        self.BotonPerfil.setGeometry(QtCore.QRect(940, 10, 75, 23))
        self.BotonPerfil.setObjectName("BotonPerfil")

        # Etiqueta para el nombre de la empresa
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label_2.setStyleSheet("\n"
                                   "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "color:(#C6DCF4)")
        self.label_2.setObjectName("label_2")

        # Frame lateral izquierdo con las opciones
        self.frame_3 = QtWidgets.QFrame(parent=self.NameEmpresa)
        self.frame_3.setGeometry(QtCore.QRect(0, 50, 201, 791))
        self.frame_3.setStyleSheet("background-color: rgb(52,58,64)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        # Etiqueta para las secciones
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 120, 111, 31))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                 "color:#C2C7D0")
        self.label.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        # Botones para las distintas secciones
        self.Administracion = QtWidgets.QPushButton(parent=self.frame_3)
        self.Administracion.setEnabled(True)
        self.Administracion.setGeometry(QtCore.QRect(0, 180, 201, 41))
        self.Administracion.setAutoFillBackground(False)
        self.Administracion.setStyleSheet("color:#C2C7D0\n"
                                          "")
        self.Administracion.setObjectName("Administracion")

        self.usuarios = QtWidgets.QPushButton(parent=self.frame_3)
        self.usuarios.setEnabled(True)
        self.usuarios.setGeometry(QtCore.QRect(0, 250, 201, 41))
        self.usuarios.setAutoFillBackground(False)
        self.usuarios.setStyleSheet("color:#C2C7D0\n"
                                    "")
        self.usuarios.setObjectName("usuarios")

        self.Ventas = QtWidgets.QPushButton(parent=self.frame_3)
        self.Ventas.setEnabled(True)
        self.Ventas.setGeometry(QtCore.QRect(0, 320, 201, 41))
        self.Ventas.setAutoFillBackground(False)
        self.Ventas.setStyleSheet("color:#C2C7D0\n"
                                  "")
        self.Ventas.setObjectName("Ventas")

        self.Devoluciones = QtWidgets.QPushButton(parent=self.frame_3)
        self.Devoluciones.setEnabled(True)
        self.Devoluciones.setGeometry(QtCore.QRect(0, 460, 201, 41))
        self.Devoluciones.setAutoFillBackground(False)
        self.Devoluciones.setStyleSheet("color:#C2C7D0\n"
                                        "")
        self.Devoluciones.setObjectName("Devoluciones")

        self.Compras = QtWidgets.QPushButton(parent=self.frame_3)
        self.Compras.setEnabled(True)
        self.Compras.setGeometry(QtCore.QRect(0, 390, 201, 41))
        self.Compras.setAutoFillBackground(False)
        self.Compras.setStyleSheet("color:#C2C7D0\n"
                                   "")
        self.Compras.setObjectName("Compras")

        self.Almacen = QtWidgets.QPushButton(parent=self.frame_3)
        self.Almacen.setEnabled(True)
        self.Almacen.setGeometry(QtCore.QRect(0, 540, 201, 41))
        self.Almacen.setAutoFillBackground(False)
        self.Almacen.setStyleSheet("color:#C2C7D0\n"
                                   "")
        self.Almacen.setObjectName("Almacen")

        # Frame para las páginas principales
        self.PagesFrame = QtWidgets.QFrame(parent=self.NameEmpresa)
        self.PagesFrame.setGeometry(QtCore.QRect(200, 50, 901, 791))
        self.PagesFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.PagesFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.PagesFrame.setObjectName("PagesFrame")

        # Stacked widget para manejar las páginas
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.PagesFrame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 901, 791))
        self.stackedWidget.setObjectName("stackedWidget")
        
        # Página 1 (administracion)
        self.page_1 = QtWidgets.QWidget()
        self.Ui_FormAdministracion =Ui_FormADMI()
        self.Ui_FormAdministracion.setupUi(self.page_1)
        self.stackedWidget.addWidget(self.page_1)

        # Página 2 (ventas)
        self.page_2 = QtWidgets.QWidget()
        self.Ui_FormUsuarios = Ui_FormUsuarios()
        self.Ui_FormUsuarios.setupUi(self.page_2)        
        self.stackedWidget.addWidget(self.page_2)
        
        # Página 3 (ventas)
        self.page_3 = QtWidgets.QWidget()
        self.Ui_FormVentas = Ui_FormVentas()
        self.Ui_FormVentas.setupUi(self.page_3)
        self.stackedWidget.addWidget(self.page_3)
        
        # Página 4 (compras)
        self.page_4 = QtWidgets.QWidget()
        self.Ui_FormCompra = Ui_FormCompra()
        self.Ui_FormCompra.setupUi(self.page_4)
        self.stackedWidget.addWidget(self.page_4)
        
        # Página 5 (devoluciones)
        self.page_5 = QtWidgets.QWidget()
        self.Ui_FormDevoluciones = Ui_FormDevoluciones()
        self.Ui_FormDevoluciones.setupUi(self.page_5)
        self.stackedWidget.addWidget(self.page_5)
        
        # Página 6 (almacen)
        self.page_6 = QtWidgets.QWidget()
        self.Ui_FormAlmacen = Ui_FormAmacenf()
        self.Ui_FormAlmacen.setupUi(self.page_6)
        self.stackedWidget.addWidget(self.page_6)

        # Configuración del widget central de la ventana principal
        MainWindow.setCentralWidget(self.centralwidget)

        # Conexión de señales y slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #conectar botones a funciones
        self.Administracion.clicked.connect(self.showAdministracion)
        self.usuarios.clicked.connect(self.showUsuarios)
        self.Ventas.clicked.connect(self.showVentas)
        self.Compras.clicked.connect(self.showCompras)
        self.Devoluciones.clicked.connect(self.showDevoluciones)
        self.Almacen.clicked.connect(self.showAlmacen)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BottonSalir.setText(_translate("MainWindow", "Salir"))
        self.BotonPerfil.setText(_translate("MainWindow", "Perfil"))
        self.label_2.setText(_translate("MainWindow", "Empresa"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Secciones</span></p></body></html>"))
        self.Administracion.setText(_translate("MainWindow", "Administracion"))
        self.usuarios.setText(_translate("MainWindow", "Usuarios"))
        self.Ventas.setText(_translate("MainWindow", "Ventas"))
        self.Devoluciones.setText(_translate("MainWindow", "Devoluciones"))
        self.Compras.setText(_translate("MainWindow", "compras"))
        self.Almacen.setText(_translate("MainWindow", "Almacen"))
        
    def showAdministracion(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showUsuarios(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def showVentas(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def showCompras(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def showDevoluciones(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def showAlmacen(self):
        self.stackedWidget.setCurrentIndex(5)
