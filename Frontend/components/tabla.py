from PyQt6 import QtCore, QtWidgets

class tabla(object):
    def tabla(self, parent, col_count, row_count, posx, posy, width, height, name, headers):
        self.tabla_usuarios = QtWidgets.QTableWidget(parent)
        self.tabla_usuarios.setGeometry(QtCore.QRect(posx, posy, width, height))
        self.tabla_usuarios.setObjectName(name)
        self.tabla_usuarios.setColumnCount(col_count)
        self.tabla_usuarios.setRowCount(row_count)

        self.headers = headers
        for i, header in enumerate(self.headers):
            item = QtWidgets.QTableWidgetItem(header)
            self.tabla_usuarios.setHorizontalHeaderItem(i, item)

        self.tabla_usuarios.setStyleSheet("color: #232f34; background-color: transparent;")

        header_style = """
            font-weight: bold;
            border-bottom: 2px solid white;
        """
        self.tabla_usuarios.horizontalHeader().setStyleSheet(header_style)

        # Aplicar borde derecho blanco a todas las celdas de las columnas, excepto la última
        cell_style = """
            border-right: 1px solid white;
        """
        for col in range(col_count - 1):
            for row in range(row_count):
                item = self.tabla_usuarios.item(row, col)
                if item:
                    item.setBackground(QtCore.Qt.GlobalColor.transparent)
                    item.setStyleSheet(cell_style)

        return self.tabla_usuarios
