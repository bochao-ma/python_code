# -*- coding: utf-8 -*-
"""
UI设计模板
"""
from ui import Ui_MainWindow  # 从Qt里面导入类
from PyQt5 import QtWidgets, QtGui
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

