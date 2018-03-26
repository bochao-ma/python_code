# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 251, 201))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.baiduyun)
        self.pushButton_2.clicked.connect(MainWindow.soft360)
        self.pushButton_3.clicked.connect(MainWindow.ruanmeisoft)
        self.pushButton_4.clicked.connect(MainWindow.ruanmeilaji)
        self.pushButton_5.clicked.connect(MainWindow.softdelete)
        self.pushButton_6.clicked.connect(MainWindow.dns360)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快捷工具"))
        self.groupBox.setTitle(_translate("MainWindow", "点击打开应用"))
        self.pushButton.setText(_translate("MainWindow", "百度云"))
        self.pushButton_3.setText(_translate("MainWindow", "软媒软件管家"))
        self.pushButton_2.setText(_translate("MainWindow", "360软件管家"))
        self.pushButton_4.setText(_translate("MainWindow", "软媒垃圾清理"))
        self.pushButton_5.setText(_translate("MainWindow", "软件卸载"))
        self.pushButton_6.setText(_translate("MainWindow", "360DNS优选"))

