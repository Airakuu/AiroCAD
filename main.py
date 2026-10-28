from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QDialog,QMainWindow,QGraphicsScene
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

        for x in range(-10000, 100001, 50):
            self.scene.addLine(x, -10000, x, 10000)
        for y in range(-10000, 10000, 50):
                self.scene.addLine(-10000, y, 10000, y)
  

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Cad()
    window.show()
    sys.exit(app.exec())