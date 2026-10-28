from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PySide6.QtGui import QPen, QColor, QTransform, QFont
from uii.ui_newmain_scene import Ui_AiroCAD
import sys

#!pyside6-designer открытие редактора
#!pyside6-uic name.ui -o ui_name.py преобразование
#!pyside6-uic main_scene.ui -o ui_main_scene.py
#!Rename-Item "C:\Users\Airakuu\Desktop\GeoMod\.venv\Lib\site-packages\PySide6\translations\designer_ru.qm.bak" "designer_ru.qm"
# ?вернуть русский язык в Qt Designer, если он пропал после обновления PySide6


class Cad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AiroCAD()
        self.ui.setupUi(self)
        self.lines = []
        self.ui.btn_createLine.clicked.connect(self.create_line)
        self.ui.btn_deleteLine.clicked.connect(self.delete_line)
        self.scene = QGraphicsScene(self)
        self.pixel_per_unit = 10  #!шаг сетки
        self.ui.graphic.setScene(self.scene)
        self.ui.graphic.scale(1, -1)
        self.scene.setSceneRect(-10000, -10000, 20000, 20000)
        self.draw_grid()
        self.ui.graphic.centerOn(0, 0)

    def draw_grid(self):
        grid_pen = QPen(QColor(200, 200, 200))
        size_axis_number = 10
        axis_pen = QPen(QColor(0, 0, 0))
        text_color = QColor(0, 0, 0)
        step = self.pixel_per_unit
        label_step = 5 * step
        axis_pen.setWidth(2)
        font = QFont("Arial", size_axis_number)
        font.setBold(True)

        for x in range(-10000, 10001, step):
            self.scene.addLine(x, -10000, x, 10000, grid_pen)
        for y in range(-10000, 10001, step):
            self.scene.addLine(-10000, y, 10000, y, grid_pen)

        self.scene.addLine(-10000, 0, 10000, 0, axis_pen)
        self.scene.addLine(0, -10000, 0, 10000, axis_pen)

        for x in range(-10000, 10001, label_step):
            if x == 0:
                continue
            self.scene.addLine(x, 3, x, -3, axis_pen)
            number = self.scene.addText(str(x // step))
            number.setFont(font)
            number.setDefaultTextColor(text_color)
            number.setTransform(QTransform.fromScale(1, -1))
            number.setPos(x - number.boundingRect().width() / 2, 0)
        for y in range(-10000, 10001, label_step):
            if y == 0:
                continue
            self.scene.addLine(3, y, -3, y, axis_pen)
            number = self.scene.addText(str(y // step))
            number.setFont(font)
            number.setDefaultTextColor(text_color)
            number.setTransform(QTransform.fromScale(1, -1))
            number.setPos(0, y + number.boundingRect().height() / 2)

    def create_line(self):
        x1 = self.ui.doubleSpinBox_x1.value() * self.pixel_per_unit
        x2 = self.ui.doubleSpinBox_x2.value() * self.pixel_per_unit
        y1 = self.ui.doubleSpinBox_y1.value() * self.pixel_per_unit
        y2 = self.ui.doubleSpinBox_y2.value() * self.pixel_per_unit
        line_pen = QPen(QColor(0, 100, 255))
        line_pen.setWidth(2)
        line = self.scene.addLine(x1, y1, x2, y2, line_pen)
        self.lines.append(line)

    def delete_line(self):
        if self.lines:
            dl = self.lines.pop()
            self.scene.removeItem(dl)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cad()
    window.show()
    sys.exit(app.exec())
