from PyQt6.QtWidgets import QComboBox, QLabel

class comboBox(object):
    
    def comboBox(self, lista, funcion):
        # Crear el ComboBox
            self.combo = QComboBox()
            
            self.combo.addItem("Selecciona un elemento")
            self.combo.addItems(lista)
            
            #self.combo.currentIndexChanged.connect(funcion)
            self.combo.setStyleSheet("padding: 8px; font-weight: bold; background-color: #ffffff; color: #000000;")
        
            return self.combo
        
    def comboBoxPaises(self, lista, funcion):
        # Crear el ComboBox
            self.combo_paises = QComboBox()
            
            self.combo_paises.addItem("Selecciona un país")
            self.combo_paises.addItems(lista)
            
            
            self.combo_paises.currentIndexChanged.connect(funcion)
            self.combo_paises.setStyleSheet("padding: 8px; font-weight: bold; background-color: #ffffff; color: #000000;")
        
            return self.combo_paises
    def comboBoxCiudades(self, lista, funcion):
        # Crear el ComboBox
            self.combo_ciudades = QComboBox()
            
            self.combo_ciudades.addItem("Selecciona una ciudad")
            self.combo_ciudades.addItems(lista)
            
            
            self.combo_ciudades.currentIndexChanged.connect(funcion)
            self.combo_ciudades.setStyleSheet("padding: 8px; font-weight: bold; background-color: #ffffff; color: #000000;")
        
            return self.combo_ciudades
    
    def labelForm(self, name, textColor):
        label = QLabel(name + ":")
        label.setStyleSheet("padding: 10px; font-weight: bold; color: " + textColor + "; ")
        return label        



