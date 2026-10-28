# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newmain_scene.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

from cad_view import CadView

class Ui_AiroCAD(object):
    def setupUi(self, AiroCAD):
        if not AiroCAD.objectName():
            AiroCAD.setObjectName(u"AiroCAD")
        AiroCAD.resize(1000, 800)
        AiroCAD.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(AiroCAD)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_line = QLabel(self.centralwidget)
        self.label_line.setObjectName(u"label_line")
        font = QFont()
        font.setPointSize(15)
        self.label_line.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_line)

        self.btn_createLine = QPushButton(self.centralwidget)
        self.btn_createLine.setObjectName(u"btn_createLine")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_createLine.sizePolicy().hasHeightForWidth())
        self.btn_createLine.setSizePolicy(sizePolicy)
        self.btn_createLine.setMinimumSize(QSize(100, 0))
        self.btn_createLine.setMaximumSize(QSize(120, 16777215))
        self.btn_createLine.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout_2.addWidget(self.btn_createLine)

        self.btn_deleteLine = QPushButton(self.centralwidget)
        self.btn_deleteLine.setObjectName(u"btn_deleteLine")
        sizePolicy.setHeightForWidth(self.btn_deleteLine.sizePolicy().hasHeightForWidth())
        self.btn_deleteLine.setSizePolicy(sizePolicy)
        self.btn_deleteLine.setMinimumSize(QSize(100, 0))
        self.btn_deleteLine.setMaximumSize(QSize(120, 16777215))
        self.btn_deleteLine.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_2.addWidget(self.btn_deleteLine)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgets_settings = QWidget(self.centralwidget)
        self.widgets_settings.setObjectName(u"widgets_settings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widgets_settings.sizePolicy().hasHeightForWidth())
        self.widgets_settings.setSizePolicy(sizePolicy1)
        self.widgets_settings.setMinimumSize(QSize(220, 0))
        self.widgets_settings.setMaximumSize(QSize(260, 16777215))
        self.label_settings = QLabel(self.widgets_settings)
        self.label_settings.setObjectName(u"label_settings")
        self.label_settings.setGeometry(QRect(20, 0, 151, 21))
        self.rbtn_dec = QRadioButton(self.widgets_settings)
        self.rbtn_dec.setObjectName(u"rbtn_dec")
        self.rbtn_dec.setGeometry(QRect(10, 30, 98, 24))
        self.rbtn_dec.setChecked(True)
        self.rbtn_pol = QRadioButton(self.widgets_settings)
        self.rbtn_pol.setObjectName(u"rbtn_pol")
        self.rbtn_pol.setGeometry(QRect(110, 30, 111, 24))
        self.doubleSpinBox_x1 = QDoubleSpinBox(self.widgets_settings)
        self.doubleSpinBox_x1.setObjectName(u"doubleSpinBox_x1")
        self.doubleSpinBox_x1.setGeometry(QRect(110, 100, 94, 26))
        self.doubleSpinBox_y1 = QDoubleSpinBox(self.widgets_settings)
        self.doubleSpinBox_y1.setObjectName(u"doubleSpinBox_y1")
        self.doubleSpinBox_y1.setGeometry(QRect(110, 140, 94, 26))
        self.doubleSpinBox_x2 = QDoubleSpinBox(self.widgets_settings)
        self.doubleSpinBox_x2.setObjectName(u"doubleSpinBox_x2")
        self.doubleSpinBox_x2.setGeometry(QRect(110, 200, 94, 26))
        self.doubleSpinBox_y2 = QDoubleSpinBox(self.widgets_settings)
        self.doubleSpinBox_y2.setObjectName(u"doubleSpinBox_y2")
        self.doubleSpinBox_y2.setGeometry(QRect(110, 230, 94, 26))
        self.label_p1 = QLabel(self.widgets_settings)
        self.label_p1.setObjectName(u"label_p1")
        self.label_p1.setGeometry(QRect(18, 70, 131, 20))
        self.label_p2 = QLabel(self.widgets_settings)
        self.label_p2.setObjectName(u"label_p2")
        self.label_p2.setGeometry(QRect(20, 180, 101, 20))
        self.label_corner = QLabel(self.widgets_settings)
        self.label_corner.setObjectName(u"label_corner")
        self.label_corner.setGeometry(QRect(20, 270, 111, 20))
        self.comboBox_corner = QComboBox(self.widgets_settings)
        self.comboBox_corner.setObjectName(u"comboBox_corner")
        self.comboBox_corner.setGeometry(QRect(20, 300, 131, 26))
        self.label_net = QLabel(self.widgets_settings)
        self.label_net.setObjectName(u"label_net")
        self.label_net.setGeometry(QRect(20, 330, 121, 16))
        self.spinBox_net = QSpinBox(self.widgets_settings)
        self.spinBox_net.setObjectName(u"spinBox_net")
        self.spinBox_net.setGeometry(QRect(20, 360, 78, 26))
        self.label = QLabel(self.widgets_settings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 100, 49, 16))
        self.label_2 = QLabel(self.widgets_settings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 49, 16))
        self.label_3 = QLabel(self.widgets_settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 210, 49, 16))
        self.label_4 = QLabel(self.widgets_settings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 240, 49, 16))

        self.horizontalLayout.addWidget(self.widgets_settings)

        self.graphic = CadView(self.centralwidget)
        self.graphic.setObjectName(u"graphic")
        self.graphic.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.graphic)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)
        AiroCAD.setCentralWidget(self.centralwidget)

        self.retranslateUi(AiroCAD)

        QMetaObject.connectSlotsByName(AiroCAD)
    # setupUi

    def retranslateUi(self, AiroCAD):
        AiroCAD.setWindowTitle(QCoreApplication.translate("AiroCAD", u"MainWindow", None))
        self.label_line.setText(QCoreApplication.translate("AiroCAD", u"\u041e\u0442\u0440\u0435\u0437\u043e\u043a", None))
        self.btn_createLine.setText(QCoreApplication.translate("AiroCAD", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.btn_deleteLine.setText(QCoreApplication.translate("AiroCAD", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_settings.setText(QCoreApplication.translate("AiroCAD", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.rbtn_dec.setText(QCoreApplication.translate("AiroCAD", u"\u0414\u0435\u043a\u0430\u0440\u0442\u043e\u0432\u0430", None))
        self.rbtn_pol.setText(QCoreApplication.translate("AiroCAD", u"\u041f\u043e\u043b\u044f\u0440\u043d\u0430\u044f", None))
        self.label_p1.setText(QCoreApplication.translate("AiroCAD", u"\u041f\u0435\u0440\u0432\u0430\u044f \u0442\u043e\u0447\u043a\u0430", None))
        self.label_p2.setText(QCoreApplication.translate("AiroCAD", u"\u0412\u0442\u043e\u0440\u0430\u044f \u0442\u043e\u0447\u043a\u0430", None))
        self.label_corner.setText(QCoreApplication.translate("AiroCAD", u"\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0443\u0433\u043b\u0430", None))
        self.label_net.setText(QCoreApplication.translate("AiroCAD", u"\u0428\u0430\u0433 \u0441\u0435\u0442\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("AiroCAD", u"X1:", None))
        self.label_2.setText(QCoreApplication.translate("AiroCAD", u"Y1:", None))
        self.label_3.setText(QCoreApplication.translate("AiroCAD", u"X2:", None))
        self.label_4.setText(QCoreApplication.translate("AiroCAD", u"Y2:", None))
    # retranslateUi

