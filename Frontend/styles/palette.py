from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPalette, QColor


class Palette:
    def __init__(self):
        self.palette = QPalette()
        self.setup_colors()
        
    def setup_colors(self):    
        self.primaryColor= "#3700B3"
        self.secondaryColor = "#03dac5"
        self.darkTextColor = "#232f34"
        self.lightTextColor = "#ffffff"
        self.enhancedTextColor1 = "#6200ee"
        self.enhancedTextColor2 = "#720d5d"
        self.enhancedTextColor3 = "#f9aa33"
        self.enhancedTextColor4 = "#37966f"
        self.lighBackgroundColor1 = "#E3F2FD"
        self.lighBackgroundColor2 = "#BBDEFB"
        self.lighterBackgroundColor = "#B2DFDB"
        self.lightBackgroundColor = "#C8E6C9"
        self.backgroundColor = "#DCEDC8"
        self.darkBackgroundColor = "#FFCCBC"
        self.darkerBackgroundColor = "#FFAB91"
        self.darkestBackgroundColor = "#FF8A65"
        self.softBlueLight = "#BBDEFB"
        self.backgroundColor1 = "rgb(246, 244, 249)"
        self.backgroundColor2 = "rgb(232, 230, 235)"
        self.backgroundColor3 = "rgb(218, 216, 221)"
        self.backgroundColor4 = "rgb(204, 202, 207)"
        self.backgroundColor5 = "rgb(190, 188, 193)"
        self.backgroundColor6 = "rgb(176, 174, 179)"
        self.backgroundColor7 = "rgb(162, 160, 165)"
        self.backgroundColor8 = "rgb(148, 146, 151)"
        self.backgroundColor9 = "rgb(134, 132, 137)"
        self.backgroundColor10 = "rgb(120, 118, 123)"
        self.backgroundColor11 = "rgb(106, 104, 109)"
        self.backgroundColor12 = "rgb(92, 90, 95)"
        self.backgroundColor13 = "rgb(78, 76, 81)"
        self.backgroundColor14 = "rgb(64, 62, 67)"
        self.backgroundColor15 = "rgb(50, 48, 53)"
        self.backgroundColor16 = "rgb(36, 34, 39)"
        self.backgroundColor17 = "rgb(22, 20, 25)"
        self.backgroundColor18 = "rgb(8, 6, 11)"

        