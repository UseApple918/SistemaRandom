import sys
from typing import Optional
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class Main_Label(QLabel):
    def __init__(self, texto):
        super().__init__(texto)

class Posiciones(QVBoxLayout):
    def __init__(self, Label):
        super().__init__()
        self.addWidget(Label)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numero Aleatorio")
        icon_path = "C:\\Users\\HPCar\\Documents\\Sistema_Contable\\Sistema_Contable (Grafico)\\Interrogacion.png"
        self.setWindowIcon(QIcon(icon_path))
        self.apply_custom_style()
        Texto1 = Main_Label("Contenido nuevo: ")
        Horizontal = Posiciones(Texto1)
        self.setLayout(Horizontal)  # Establecer el layout de la ventana principal

    def apply_custom_style(self):
        self.setStyleSheet('background-color: lightblue;')

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.setStyle("Fusion")
app.exec_()

   
    