from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QDialog,QMainWindow,QGraphicsScene
from PySide6.QtGui import QPen,QColor,QTransform
from uii.ui_main_scene import Ui_main_scene
import sys
#!pyside6-designer открытие редактора
#!pyside6-uic name.ui -o ui_name.py преобразование
#!pyside6-uic main_scene.ui -o ui_main_scene.py
#!Rename-Item "C:\Users\Airakuu\Desktop\GeoMod\.venv\Lib\site-packages\PySide6\translations\designer_ru.qm.bak" "designer_ru.qm" 
#?вернуть русский язык в Qt Designer, если он пропал после обновления PySide6



class Cad(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_scene()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        self.ui.graphic.setScene(self.scene)
        self.ui.graphic.scale(1, -1)
        self.scene.setSceneRect(-400, -300, 800, 600)
        self.draw_grid()
    def draw_grid(self):
        grid_pen=QPen(QColor(200,200,200))
        axis_pen=QPen(QColor(0,0,0))
        text_color=QColor(0,0,0)
        
        axis_pen.setWidth(2)    
        for x in range(-10000, 100001, 50):
            self.scene.addLine(x, -10000, x, 10000, grid_pen)
        for y in range(-10000, 10000, 50):
            self.scene.addLine(-10000, y, 10000, y, grid_pen)
        self.scene.addLine(-10000,0,10000,0,axis_pen)
        self.scene.addLine(0,-10000,0,10000,axis_pen)
        number = self.scene.addText("100")
        number.setDefaultTextColor(text_color)
        number.setPos(100 - number.boundingRect().width() / 2, 0)
        number.setScale(1)
        number.setTransform(QTransform.fromScale(1,-1))
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Cad()
    window.show()
    sys.exit(app.exec())