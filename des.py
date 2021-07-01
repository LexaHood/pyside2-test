# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 220)
        MainWindow.setMinimumSize(QSize(550, 220))
        MainWindow.setMaximumSize(QSize(550, 220))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 421, 20))
        self.lineEdit.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 40, 75, 23))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 110, 421, 20))
        self.lineEdit_2.setReadOnly(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 110, 75, 23))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 161, 16))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 180, 75, 23))
        self.pushButton_3.setCheckable(False)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 150, 211, 20))
        self.label_3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Test Task Dev", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0435\u0440\u0432\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a\u043e \u0432\u0442\u043e\u0440\u043e\u043c\u0443 \u0444\u0430\u0439\u043b\u0443", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.label_3.setText("")
    # retranslateUi

