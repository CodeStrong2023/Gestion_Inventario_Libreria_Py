from PyQt6 import QtCore, QtWidgets

class Widget(object):
        def createWidget (self, name):
                self.createWidget = QtWidgets.QWidget()
                self.createWidget.setObjectName(name)
                
                return self.createWidget

        def createStackedWidget(self, parent, posx, posy, width, height ,name):
                self.createStackedWidget = QtWidgets.QStackedWidget(parent=parent)
                self.createStackedWidget.setGeometry(QtCore.QRect(posx, posy, width, height))
                self.createStackedWidget.setObjectName(name)
                return self.createStackedWidget