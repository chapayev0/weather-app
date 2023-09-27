# -*- coding: utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

import sys
import sqlite3
import os

from ui.ui_main import *

class main_ui(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()


                event.accept()

        self.ui.frame.mouseMoveEvent = move_window

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)


        # Button commandsgoes here

        self.ui.close_btn.clicked.connect(self.exit_fun)



    def exit_fun(self):

        self.close()

    def mousePressEvent(self, event):

        self.dragpos = event.globalPos()
        self.setWindowOpacity(0.9)

    def mouseReleaseEvent(self, event):
        self.setWindowOpacity(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = main_ui()

    window.show()

    sys.exit(app.exec_())