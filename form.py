# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(255, 240, 242)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 781, 371))
        self.textBrowser.setObjectName("textBrowser")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(100, 470, 221, 71))
        self.start_button.setStyleSheet("font-size: 30px;\n"
"font-weight: bolder;\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color: rgb(1, 255, 225);\n"
"background-color: rgb(255, 92, 17);\n"
"color: rgb(255, 255, 255)")
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(440, 470, 221, 71))
        self.stop_button.setStyleSheet("font-size: 30px;\n"
"font-weight: bolder;\n"
"border: 2px solid;\n"
"border-radius: 20px;\n"
"border-color: rgb(1, 255, 225);\n"
"background-color: rgb(255, 92, 17);\n"
"color: rgb(255, 255, 255)")
        self.stop_button.setObjectName("stop_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 390, 91, 20))
        self.label.setStyleSheet("font: 75 18pt \"MS Sans Serif\";\n"
"justify-content:center;\n"
"align-items: center;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(220, 430, 354, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDick = QtWidgets.QLabel(self.widget)
        self.labelDick.setStyleSheet("font: 75 18pt \"MS Sans Serif\";")
        self.labelDick.setObjectName("labelDick")
        self.horizontalLayout.addWidget(self.labelDick)
        self.line_from = QtWidgets.QLineEdit(self.widget)
        self.line_from.setStyleSheet("z-index: 9999;")
        self.line_from.setObjectName("line_from")
        self.horizontalLayout.addWidget(self.line_from)
        self.labelCunt = QtWidgets.QLabel(self.widget)
        self.labelCunt.setStyleSheet("font: 75 18pt \"MS Sans Serif\";")
        self.labelCunt.setObjectName("labelCunt")
        self.horizontalLayout.addWidget(self.labelCunt)
        self.line_to = QtWidgets.QLineEdit(self.widget)
        self.line_to.setStyleSheet("z-index: 9999;")
        self.line_to.setObjectName("line_to")
        self.horizontalLayout.addWidget(self.line_to)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "   TIME"))
        self.labelDick.setText(_translate("MainWindow", "from"))
        self.labelCunt.setText(_translate("MainWindow", "to"))
