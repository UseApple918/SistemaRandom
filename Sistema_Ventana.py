import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget , QPushButton , QLabel , QStyle
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numero Aleatorio")
        icon_path = "C:\\Users\\HPCar\\Documents\\Sistema_Contable\\Sistema_Contable (Grafico)\\Interrogacion.png"
        self.setWindowIcon(QIcon(icon_path)) 
        self.apply_custom_style()
    def apply_custom_style(self):
        QStyle.children()
        
                
        
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()    
    