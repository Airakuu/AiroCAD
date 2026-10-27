from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QMainWindow
from uii.ui_calc import Ui_MainWindow
import sys
#!pyside6-designer открытие редактора
#!pyside6-uic name.ui -o ui_name.py преобразование
 



class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_number = ""
        
        
        for number in range(10):
            btn = getattr(self.ui,f"btn_{number}")
            btn.clicked.connect(
                lambda checked=False,d=number:self.add_number(str(d))
            )
        
        
    def add_number(self,number):
        self.current_number += number
        self.ui.label_result.setText(self.current_number)




    
    

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Calc()
    window.show()
    sys.exit(app.exec_())