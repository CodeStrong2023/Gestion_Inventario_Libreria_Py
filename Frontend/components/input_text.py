from PyQt6 import QtCore, QtWidgets

class inputText(object):
    def inputText(self, parent, posx, posy, width, height, name):
        self.inputText = QtWidgets.QLineEdit(parent=parent)
        self.inputText.setGeometry(QtCore.QRect(posx, posy, width, height))
        self.inputText.setObjectName(name)
        return self.inputText
    
    def inputForm(self, parent, posx, posy, width, height, name, textColor, backgroundColor, sing, value ="",actualizar=False):
        
        self.input_nombre_empresa = inputText().inputText(parent, posx, posy, width, height, name)
        if actualizar:
            self.input_nombre_empresa.setText(value)
        else:
            self.input_nombre_empresa.setPlaceholderText(name +" de " + sing)        
        
        
        self.input_nombre_empresa.setStyleSheet("padding: 8px; font-weight: bold;"+"background-color: " + backgroundColor + "; color: " + textColor + "; ")
        
        return self.input_nombre_empresa
    
    def labelForm(self, name, textColor):
        self.label_nombre = QtWidgets.QLabel(name+":")
        self.label_nombre.setStyleSheet("padding: 10px; font-weight: bold;"+"color: " + textColor + "; ")
        
        return self.label_nombre
        

        
