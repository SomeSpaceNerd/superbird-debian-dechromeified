# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Button1 = QLabel(self.centralwidget)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setGeometry(QRect(0, 0, 160, 20))
        self.Button1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Button2 = QLabel(self.centralwidget)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(160, 0, 160, 20))
        self.Button2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Button3 = QLabel(self.centralwidget)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setGeometry(QRect(320, 0, 160, 20))
        self.Button3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Button4 = QLabel(self.centralwidget)
        self.Button4.setObjectName(u"Button4")
        self.Button4.setGeometry(QRect(480, 0, 160, 20))
        self.Button4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Button5 = QLabel(self.centralwidget)
        self.Button5.setObjectName(u"Button5")
        self.Button5.setGeometry(QRect(640, 0, 160, 20))
        self.Button5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MenuButton = QLabel(self.centralwidget)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setGeometry(QRect(680, 450, 120, 20))
        font = QFont()
        font.setPointSize(13)
        self.MenuButton.setFont(font)
        self.KnobLabel = QLabel(self.centralwidget)
        self.KnobLabel.setObjectName(u"KnobLabel")
        self.KnobLabel.setGeometry(QRect(580, 190, 50, 20))
        self.KnobLabel.setFont(font)
        self.Knob = QLabel(self.centralwidget)
        self.Knob.setObjectName(u"Knob")
        self.Knob.setGeometry(QRect(580, 210, 50, 20))
        font1 = QFont()
        font1.setPointSize(9)
        self.Knob.setFont(font1)
        self.OpenGL_Demo = QOpenGLWidget(self.centralwidget)
        self.OpenGL_Demo.setObjectName(u"OpenGL_Demo")
        self.OpenGL_Demo.setGeometry(QRect(0, 180, 300, 300))
        self.OpenGL_Label = QLabel(self.centralwidget)
        self.OpenGL_Label.setObjectName(u"OpenGL_Label")
        self.OpenGL_Label.setGeometry(QRect(0, 160, 90, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Button1.setText(QCoreApplication.translate("MainWindow", u"Button 1", None))
        self.Button2.setText(QCoreApplication.translate("MainWindow", u"Button 2", None))
        self.Button3.setText(QCoreApplication.translate("MainWindow", u"Button 3", None))
        self.Button4.setText(QCoreApplication.translate("MainWindow", u"Button 4", None))
        self.Button5.setText(QCoreApplication.translate("MainWindow", u"Button 5", None))
        self.MenuButton.setText(QCoreApplication.translate("MainWindow", u"MenuButton", None))
        self.KnobLabel.setText(QCoreApplication.translate("MainWindow", u"Knob", None))
        self.Knob.setText(QCoreApplication.translate("MainWindow", u"Knob", None))
        self.OpenGL_Label.setText(QCoreApplication.translate("MainWindow", u"openGL Demo", None))
    # retranslateUi

