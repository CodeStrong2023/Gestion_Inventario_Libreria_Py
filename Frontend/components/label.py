from PyQt6 import QtCore, QtWidgets

class label(object):
    def label(self, parent, posx, posy, width, height, name):
        self.label = QtWidgets.QLabel(parent=parent)
        self.label.setGeometry(QtCore.QRect(posx, posy, width, height))
        self.label.setObjectName(name)
        
        return self.label