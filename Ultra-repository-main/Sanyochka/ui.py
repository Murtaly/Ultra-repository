# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(519, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MATYE = QtWidgets.QCheckBox(self.centralwidget)
        self.MATYE.setGeometry(QtCore.QRect(140, 230, 271, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MATYE.sizePolicy().hasHeightForWidth())
        self.MATYE.setSizePolicy(sizePolicy)
        self.MATYE.setMinimumSize(QtCore.QSize(0, 0))
        self.MATYE.setBaseSize(QtCore.QSize(12, 12))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        self.MATYE.setFont(font)
        self.MATYE.setStyleSheet("")
        self.MATYE.setIconSize(QtCore.QSize(20, 20))
        self.MATYE.setObjectName("MATYE")
        self.BAV = QtWidgets.QCheckBox(self.centralwidget)
        self.BAV.setGeometry(QtCore.QRect(140, 280, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        self.BAV.setFont(font)
        self.BAV.setStyleSheet("\n"
"")
        self.BAV.setObjectName("BAV")
        self.DEGENERATE = QtWidgets.QPushButton(self.centralwidget)
        self.DEGENERATE.setGeometry(QtCore.QRect(180, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.DEGENERATE.setFont(font)
        self.DEGENERATE.setStyleSheet("background-color:#fbeee1;\n"
"border: 2px solid #422800;\n"
"border-radius: 10px;\n"
"color: #422800;")
        self.DEGENERATE.setObjectName("DEGENERATE")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 180, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 519, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MATYE.setText(_translate("MainWindow", "Використовувати числа"))
        self.BAV.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.DEGENERATE.setText(_translate("MainWindow", "Згенерувати"))
        self.label.setText(_translate("MainWindow", "Генератор паролів"))
        self.label_2.setText(_translate("MainWindow", "Тут буде результат"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


