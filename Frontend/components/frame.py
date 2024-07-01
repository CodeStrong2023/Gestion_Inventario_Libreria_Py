from PyQt6 import QtCore, QtWidgets

class frame(object):
    def frame(self, parent, posx, posy, width, height, style, name):
        self.frame = QtWidgets.QFrame(parent=parent)
        self.frame.setGeometry(QtCore.QRect(posx, posy, width, height))
        self.frame.setStyleSheet(style)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName(name)
        
        return self.frame