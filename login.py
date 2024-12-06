# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)
import encrypt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 383)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251,102,102, 200), stop:1  rgba(20,196,188, 210));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 261, 311))
        self.frame.setStyleSheet(u"background-color: rgb(246, 246, 246);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 170, 251, 141))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 20, 141, 31))
        font = QFont()
        font.setFamilies([u"Castellar"])
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(22,218,208);\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 82, 141, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(22,218,208);\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"font-size:14;\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 40, 131, 20))
        self.lineEdit.setStyleSheet(u"border: 1px solid rgb(22,218,208);\n"
"border-radius:10px;\n"
"color: rgb(5, 49, 97);\n"
"")
        self.lineEdit_2 = QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 80, 131, 20))
        self.lineEdit_2.setStyleSheet(u"border: 1px solid rgb(22,218,208);\n"
"border-radius:10px;\n"
"color: rgb(5, 49, 97);\n"
"")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(13, 40, 61, 20))
        font1 = QFont()
        font1.setFamilies([u"Snap ITC"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 71, 20))
        font2 = QFont()
        font2.setFamilies([u"Snap ITC"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 110, 75, 20))
        font3 = QFont()
        font3.setFamilies([u"Snap ITC"])
        font3.setBold(True)
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(22, 218, 208);")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 20, 141, 20))
        self.lineEdit_3.setStyleSheet(u"border: 1px solid rgb(22,218,208);\n"
"border-radius:10px;\n"
"color: rgb(5, 49, 97);")
        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 50, 141, 20))
        self.lineEdit_4.setStyleSheet(u"border: 1px solid rgb(22,218,208);\n"
"color: rgb(5, 49, 97);\n"
"border-radius:10px;")
        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 80, 141, 20))
        self.lineEdit_5.setStyleSheet(u"border: 1px solid rgb(22,218,208);\n"
"border-radius:10px;\n"
"color: rgb(5, 49, 97);")
        self.pushButton_3 = QPushButton(self.page_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 110, 75, 20))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(22, 218, 208);")
        self.label_5 = QLabel(self.page_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 54, 12))
        font4 = QFont()
        font4.setFamilies([u"Snap ITC"])
        font4.setPointSize(10)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 71, 16))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 54, 12))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.stackedWidget.addWidget(self.page_3)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 20, 140, 140))
        self.groupBox.setStyleSheet(u"border-radius:70px;\n"
"border:2px solid rgb(22,218,208);\n"
"background:transparent;\n"
"")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 101, 31))
        font5 = QFont()
        font5.setFamilies([u"Fixedsys"])
        font5.setPointSize(22)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"border:transparent;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 81, 81))
        self.label.setMouseTracking(False)
        self.label.setStyleSheet(u"border:transparent;\n"
"background:transparent;\n"
"")
        self.label.setPixmap(QPixmap(u":/D:/WorkSpace/image_encrypt/icons/OIP.jpg"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Name</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Password</p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Comfirm", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Comfirm", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Again", None))
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff557f;\">ENCRYPT</span></p></body></html>", None))
        self.label.setText("")
    # retranslateUi

