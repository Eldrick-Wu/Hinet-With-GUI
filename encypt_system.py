import torch
import torch.nn
import torch.optim
import torchvision
import numpy as np
from HiNet.model import *
import HiNet.config as c
import HiNet.modules.Unet_common as common
import torchvision.transforms as transforms
import os
import math

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

from sys import argv

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Main_Window import Ui_MainWindow
from PIL import Image


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('图像加密系统')
        self.stackedWidget.setCurrentIndex(0)
        net = Model().to(device)
        init_model(net)
        self.hinet = torch.nn.DataParallel(net, device_ids=[0])
        params_trainable = list(filter(lambda p: p.requires_grad, net.parameters()))
        self.optim = torch.optim.Adam(params_trainable, lr=c.lr, betas=c.betas, eps=1e-6, weight_decay=c.weight_decay)
        self.backward_z = None
        self.out_steg= None
        self.dwt = common.DWT()
        self.iwt = common.IWT()
        self.secret_image = None
        self.cover_image =None
        self.steg_img = None

        self.slots()

    def slots(self):
        self.pushButton.clicked.connect(lambda :self.open_image('secret'))
        self.pushButton_3.clicked.connect(lambda:self.open_image('cover'))
        self.pushButton_2.clicked.connect(self.encrypt_image)
        self.pushButton_4.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1))
        self.pushButton_7.clicked.connect(lambda:self.open_image('steg'))
        self.pushButton_8.clicked.connect(self.decrypt_image)
        self.pushButton_5.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))


    def encrypt_image(self):
        self.load(c.MODEL_PATH)
        self.hinet.eval()
        cover = self.load_image(self.cover_image)
        secret = self.load_image(self.secret_image)
        # 将加载的 cover 和 secret 处理为输入
        cover_input = self.dwt(cover)
        secret_input = self.dwt(secret)
        input_img = torch.cat((cover_input, secret_input), 1)
        with torch.no_grad():
            output = self.hinet(input_img)
            self.output_steg = output.narrow(1, 0, 4 * c.channels_in)
            output_z = output.narrow(1, 4 * c.channels_in, output.shape[1] - 4 * c.channels_in)
            self.steg_img = self.iwt(self.output_steg)
            self.backward_z = self.gauss_noise(output_z.shape)
            cover_np = cover.squeeze().cpu().numpy()  # 将Tensor转换为numpy
            steg_np = self.steg_img.squeeze().cpu().numpy()
            psnr_cover = self.computePSNR(cover_np, steg_np)
            self.label_4.setText(f'{psnr_cover}')
            # 创建文件夹路径
            self.create_directory(c.IMAGE_PATH_cover)
            self.create_directory(c.IMAGE_PATH_secret)
            self.create_directory(c.IMAGE_PATH_steg)
            self.create_directory(c.IMAGE_PATH_secret_rev)
            torchvision.utils.save_image(cover, c.IMAGE_PATH_cover + 'cover_image.png')
            torchvision.utils.save_image(secret, c.IMAGE_PATH_secret + 'secret_image.png')
            torchvision.utils.save_image(self.steg_img, c.IMAGE_PATH_steg + 'steg_image.png')
            pixmap = QPixmap(c.IMAGE_PATH_cover + 'cover_image.png')
            self.label_7.setPixmap(pixmap)
            self.label_7.setScaledContents(True)  # 将图片显示在 QLabel 上

    def decrypt_image(self):
        with torch.no_grad():
            secret = self.load_image(self.secret_image)
            cover = self.load_image(self.cover_image)
            output_rev = torch.cat((self.output_steg, self.backward_z), 1)
            bacward_img = self.hinet(output_rev, rev=True)
            secret_rev = bacward_img.narrow(1, 4 * c.channels_in, bacward_img.shape[1] - 4 * c.channels_in)
            secret_rev = self.iwt(secret_rev)
            cover_rev = bacward_img.narrow(1, 0, 4 * c.channels_in)
            cover_rev = self.iwt(cover_rev)
            torchvision.utils.save_image(secret_rev, c.IMAGE_PATH_secret_rev + 'secret_rev_image.png')
            pixmap = QPixmap(c.IMAGE_PATH_secret_rev + 'secret_rev_image.png')
            self.label_10.setPixmap(pixmap)
            self.label_10.setScaledContents(True)  # 将图片显示在 QLabel 上
            # 对比原始的 secret 和恢复的 secret_rev
            secret_np = secret.squeeze().cpu().numpy()  # 将Tensor转换为numpy
            secret_rev_np = secret_rev.squeeze().cpu().numpy()

            # 计算PSNR
            psnr_value = self.computePSNR(secret_np, secret_rev_np)
            print(f"隐写数据和恢复的隐写数据之间的 PSNR: {psnr_value}")

            # 计算PSNR (cover vs steg)
            cover_np = cover.squeeze().cpu().numpy()  # 将Tensor转换为numpy
            steg_np = self.steg_img.squeeze().cpu().numpy()

            psnr_cover = self.computePSNR(cover_np, steg_np)
            print(f"封面图像和隐写图像之间的 PSNR: {psnr_cover}")

            # 逐像素对比
            difference = np.abs(secret_np - secret_rev_np)
            print(f"最大像素差异: {np.max(difference)}")
            print(f"均方误差(MSE): {np.mean(difference ** 2)}")

    def open_image(self,kind):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if kind == "secret":
            if file_path:  # 如果选择了图片
                self.secret_image = Image.open(file_path).convert('RGB')
                pixmap = QPixmap(file_path)
                self.label_9.setPixmap(pixmap)
                self.label_9.setScaledContents(True)# 将图片显示在 QLabel 上
        elif kind == "cover":
            if file_path:  # 如果选择了图片
                self.cover_image = Image.open(file_path).convert('RGB')
                pixmap = QPixmap(file_path)
                self.label_8.setPixmap(pixmap)
                self.label_8.setScaledContents(True)  # 将图片显示在 QLabel 上
        elif kind == "steg":
            if file_path:  # 如果选择了图片
                self.cover_image = Image.open(file_path).convert('RGB')
                pixmap = QPixmap(file_path)
                self.label_10.setPixmap(pixmap)
                self.label_10.setScaledContents(True)  # 将图片显示在 QLabel 上



    def load(self,name):
        state_dicts = torch.load(name, map_location=device, weights_only=True)
        network_state_dict = {k: v for k, v in state_dicts['net'].items() if 'tmp_var' not in k}
        self.hinet.load_state_dict(network_state_dict)
        try:
            self.optim.load_state_dict(state_dicts['opt'])
        except:
            print('Cannot load optimizer for some reason or other')



    def gauss_noise(self,shape):
        noise = torch.zeros(shape, device=device)
        for i in range(noise.shape[0]):
            noise[i] = torch.randn(noise[i].shape, device=device)
        return noise



    def computePSNR(self,origin, pred, data_range=255):

        # 确保图像是浮动类型
        origin = np.array(origin, dtype=np.float32)
        pred = np.array(pred, dtype=np.float32)

        # 计算均方误差（MSE）
        mse = np.mean((origin - pred) ** 2)

        # 如果MSE为0，表示两图完全相同，PSNR为无穷大
        if mse == 0:
            return float('inf')

        # 计算PSNR
        psnr = 10 * math.log10((data_range ** 2) / mse)

        return psnr



    def load_image(self,image):
        """传入图片并转为张量"""
        transform = transforms.Compose([
            transforms.Resize((256, 256)),  # 调整图像大小
            transforms.ToTensor()  # 转换为张量
        ])
        return transform(image).unsqueeze(0).to(device)  # 增加batch维度并移动到device

    def create_directory(self,path):
        """如果路径不存在则创建"""
        if not os.path.exists(path):
            os.makedirs(path)


if __name__ == '__main__':
    app = QApplication(argv)
    ui = MainWindow()
    ui.show()
    app.exec()