from sys import argv
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from login import Ui_MainWindow
from encypt_system import MainWindow
from utils import *
from utils.mysql_tools import MySQLDatabase


class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("登录")
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.db = MySQLDatabase(host="localhost", user="root", password="884088haba", database="encrypt_users")
        self.slots()
    def slots(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_4.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.register)

    def login(self):
        user_name = self.lineEdit.text()
        psswd = self.lineEdit_2.text()
        user = self.db.query_users(f"user_name = '{user_name}'")
        if user is not None:
            res = self.db.query_users(f"user_name = '{user_name}' AND user_password = '{psswd}'")
            if res is not None:
                self.main_window = MainWindow()
                self.main_window.show()
                self.close()
            else:
                self.show_message('密码错误')
        else:
            self.show_message('用户不存在')

    def register(self):
        user_name = self.lineEdit_3.text()
        pwd = self.lineEdit_4.text()
        pwd_1 = self.lineEdit_5.text()
        if pwd != pwd_1:
            self.show_message('前后密码不一致')
        else:
            self.db.insert_user((user_name,pwd))
            self.show_message('注册成功')
            self.stackedWidget.setCurrentIndex(1)

    def show_message(self,message):
        # 创建提示框
        message_box = QMessageBox(self)
        message_box.setIcon(QMessageBox.Information)  # 设置图标类型
        message_box.setWindowTitle("提示")  # 设置提示框标题
        message_box.setText(message)  # 设置提示框文本
        message_box.setInformativeText("点击确定关闭")  # 设置附加信息
        message_box.setStandardButtons(QMessageBox.Ok)  # 设置按钮
        message_box.exec()  # 显示提示框并等待关闭






if __name__ == '__main__':
    app = QApplication(argv)
    ui = LoginWindow()
    ui.show()
    app.exec()