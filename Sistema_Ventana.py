import sys
from typing import Optional
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget , QPushButton , QLabel, QVBoxLayout
global ventana
class Main_Label(QLabel):
    def __init__(self, texto):
        super().__init__(texto)

class Posiciones (QVBoxLayout):
    def __init__(self, Label):
        super().__init__(Label)
          
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numero Aleatorio")
        icon_path = "C:\\Users\\HPCar\\Documents\\Sistema_Contable\\Sistema_Contable (Grafico)\\Interrogacion.png"
        self.setWindowIcon(QIcon(icon_path)) 
        self.apply_custom_style()
        Texto1 = Main_Label("Contenido nuevo: ")
        Horizontal = Posiciones(ventana)
        Horizontal.addWidget(Texto1)
    def apply_custom_style(self):
        self.setStyleSheet('background-color: lightblue;')  
ventana = MainWindow()     
app = QApplication(sys.argv)
ventana.show()
app.setStyle("Fusion")
app.exec_() 
   
    