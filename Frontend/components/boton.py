from PyQt6 import QtCore, QtWidgets

class boton(object):
    def boton(self, parent, style, texto, posx, posy, width, height ,name):
        self.boton = QtWidgets.QPushButton(parent=parent)
        self.boton.setGeometry(QtCore.QRect(posx, posy, width, height))
        self.boton.setStyleSheet(style)
        self.boton.setObjectName(name)
        self.boton.setText(texto)
        
        return self.boton
        