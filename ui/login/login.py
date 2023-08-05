import os
import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QGridLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt

class Login_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,300)

        ## 隐藏原有标题栏，自定义标题栏
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.title_bar = QWidget(self)
        self.title_bar.resize(400,30)
        # 添加图标
        current_directory = os.getcwd()
        print(current_directory)
        self.title_icon = QPixmap("./source/icon/window_icon.png").scaled(30,30,aspectMode=Qt.KeepAspectRatio)
        self.title_bar_icon_label = QLabel(self.title_bar)
        self.title_bar_icon_label.setFixedSize(30,30)
        self.title_bar_icon_label.setPixmap(self.title_icon)

        # 添加标题
        self.title_bar_title = QLabel('MMusic',self.title_bar)
        self.title_bar_title.setFixedSize(50,30)

        # 添加最小化按钮和关闭按钮
        self.mininumbutton = QPushButton('➖',self.title_bar)
        self.closebutton = QPushButton('✖',self.title_bar)
        self.mininumbutton.resize(30,30)
        self.closebutton.resize(30,30)

        # 设置布局
        self.title_bar_icon_label.move(0,0)
        self.title_bar_title.move(30,0)
        self.mininumbutton.move(340,0)
        self.closebutton.move(370,0)

        # 设置边框透明
        self.setStyleSheet("""
            QWidget{
            border: 3px solid black;
            }
            QWidget QWidget {
            border: None;
            }
        """)

        # 给最小化和关闭按钮连接鼠标点击槽函数
        self.mininumbutton.clicked.connect(self.showMinimized)
        self.closebutton.clicked.connect(self.close)









