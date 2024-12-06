# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTabWidget,
    QWidget)
import encrypt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 435)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251,102,102, 200), stop:1 rgba(20,196,188, 210));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 10, 751, 381))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fcefe8, stop:1 #fffbf0);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 731, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 120, 311))
        self.groupBox.setStyleSheet(u"border: 2px solid rgb(22,228,218);\n"
"border-radius:10px;")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 81, 30))
        self.pushButton.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon = QIcon()
        icon.addFile(u":/D:/WorkSpace/image_encrypt/icons/\u72d7\u72d7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 170, 80, 30))
        self.pushButton_2.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon1 = QIcon()
        icon1.addFile(u":/D:/WorkSpace/image_encrypt/icons/\u72d7\u5b50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 100, 80, 30))
        self.pushButton_3.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon2 = QIcon()
        icon2.addFile(u":/D:/WorkSpace/image_encrypt/icons/\u72d7\u72d7 (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 240, 80, 30))
        self.pushButton_4.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon3 = QIcon()
        icon3.addFile(u":/D:/WorkSpace/image_encrypt/icons/\u72d7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 61, 21))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(22, 228, 218);")
        self.tabWidget = QTabWidget(self.page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(230, 10, 501, 311))
        self.tabWidget.setStyleSheet(u"color: rgb(5, 49, 97);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 451, 241))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 451, 241))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 20, 451, 241))
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 340, 160, 21))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(5, 49, 97);")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.horizontalLayout.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 20, 120, 311))
        self.groupBox_2.setStyleSheet(u"border: 2px solid rgb(22,228,218);\n"
"border-radius:10px;")
        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 60, 80, 30))
        self.pushButton_7.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon4 = QIcon()
        icon4.addFile(u":/D:/WorkSpace/image_encrypt/icons/\u72d7&\u5ba0\u7269\u7528\u54c1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 150, 80, 30))
        self.pushButton_8.setStyleSheet(u"color:rgb(5, 49, 97)")
        icon5 = QIcon()
        icon5.addFile(u":/D:/WorkSpace/image_encrypt/icons/red-\u5ba0\u7269\u72d7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 230, 80, 30))
        self.pushButton_5.setStyleSheet(u"color: rgb(5, 49, 97);")
        icon6 = QIcon()
        icon6.addFile(u":/D:/WorkSpace/image_encrypt/icons/04-\u5c0f\u72d7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 20, 511, 321))
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 806, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u79d8\u5bc6\u56fe\u50cf", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u56fe\u50cf", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u63a9\u76d6\u56fe\u50cf", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6\u56fe\u50cf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u83dc\u5355</p><p align=\"center\"><br/></p></body></html>", None))
        self.label_9.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u79d8\u5bc6\u56fe\u50cf", None))
        self.label_8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u63a9\u76d6\u56fe\u50cf", None))
        self.label_7.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u56fe\u50cf", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6PSNR:", None))
        self.label_4.setText("")
        self.groupBox_2.setTitle("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u56fe\u7247", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u89e3\u5bc6", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.label_10.setText("")
    # retranslateUi

