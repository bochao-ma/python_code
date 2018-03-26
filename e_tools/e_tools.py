# -*- coding: utf-8 -*-
from untitled import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
import sys
import win32api

url_baidu = 'D:\\tool\BaiduYunGuanjia\百度云不限速.exe'
url_360dns = 'D:\\tool\DNS优选.exe'
url_360soft = "D:\Program Files (x86)\\360SoftMgr\SoftMgr\SoftMgr.exe"
url_ruanmeilaji = 'D:\\tool\软媒\cleanmaster.exe'
url_ruanmwisoft = 'D:\\tool\软媒\softmaster.exe'
url_softdelete = 'D:\\tool\TotalUninstallPortable\TotalUninstallPortable.exe'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

    def baiduyun(self):
        win32api.ShellExecute(0, 'open', url_baidu, '', '', 1)

    def ruanmeisoft(self):
        win32api.ShellExecute(0, 'open', url_ruanmwisoft, '', '', 1)

    def dns360(self):
        win32api.ShellExecute(0, 'open', url_360dns, '', '', 1)

    def ruanmeilaji(self):
        win32api.ShellExecute(0, 'open', url_ruanmeilaji, '', '', 1)

    def soft360(self):
        win32api.ShellExecute(0, 'open', url_360soft, '', '', 1)

    def softdelete(self):
        win32api.ShellExecute(0, 'open', url_softdelete, '', '', 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
