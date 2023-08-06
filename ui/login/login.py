import os
import sys

import PySide6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, \
    QVBoxLayout, QHBoxLayout,QGridLayout,QLineEdit
from PySide6.QtGui import QIcon, QPixmap, QFont, QPainter, QColor, QRegularExpressionValidator, QPalette
from PySide6.QtCore import Qt, QRegularExpression


class Login_Window(QWidget):
    def __init__(self):
        super().__init__()
        # 窗口大小
        self.resize(400,300)
        # 窗口移动参数
        self.draggable = False
        self.press_pos = None

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

        image_path = "C:\\Users\\LENOVO\\Desktop\\myimage.jpg"
        self.background_image = QPixmap(image_path)


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

        # 账号，密码，登录，注册，验证码等控件
        self.count_label = QLabel('账号',self)
        self.count = QLineEdit(self)
        self.password_label = QLabel('密码',self)
        self.password = QLineEdit(self)
        self.login_button = QPushButton('登录',self)
        self.register_button = QPushButton('注册',self)
        self.count_label.setAlignment(Qt.AlignVCenter)

        # 设置控件尺寸，外观
        self.login_button.setFixedSize(60,30)
        self.register_button.setFixedSize(60,30)
        self.count.setFixedHeight(20)
        self.password.setFixedHeight(20)
        self.count.setStyleSheet("background-color: transparent; border: 1px solid black; color: black;")
        self.password.setStyleSheet("background-color: transparent; border: 1px solid black; color: black;")

        # 设置字体
        label_font = QFont()
        label_font.setPointSize(10)
        # 使用 QPalette 设置字体颜色
        palette = self.count_label.palette()
        palette.setColor(self.count_label.foregroundRole(), QColor(255, 0, 0))  # 设置字体颜色为红色
        self.count_label.setPalette(palette)
        self.password_label.setPalette(palette)
        self.count_label.setFont(label_font)
        self.password_label.setFont(label_font)


        # 账号布局
        c_layout = QHBoxLayout()
        c_layout.addWidget(self.count_label)
        c_layout.addWidget(self.count)
        c_layout.setSpacing(15)

        # 密码布局
        p_layout = QHBoxLayout()
        p_layout.addWidget(self.password_label)
        p_layout.addWidget(self.password)
        p_layout.setSpacing(15)

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        button_layout.setSpacing(50)

        # 添加一个空的 QLabel 充当额外的空白，增加垂直空间
        empty_label = QLabel(self)
        empty_label.setMinimumHeight(10)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(c_layout)
        v_layout.addLayout(p_layout)
        v_layout.addWidget(empty_label)
        v_layout.addLayout(button_layout)
        v_layout.setContentsMargins(100, 80, 100, 50)
        v_layout.setSpacing(20)
        v_layout.addStretch(1)  # 添加占位符，使控件居中显示

        # 设置按钮样式表显示轮廓
        self.login_button.setStyleSheet("border: 2px solid black; background-color: lightblue;")
        self.register_button.setStyleSheet("border: 2px solid black; background-color: lightblue;")

        # 使用Qt验证器对帐号文本框进行输入内容检测，使之只能输入十位阿拉伯数字
        # 创建 QRegularExpressionValidator，并设置正则表达式
        regex = QRegularExpression("^[0-9]{10}$")  # 10位数字的正则表达式
        validator = QRegularExpressionValidator(regex, self)
        self.count.setValidator(validator)



    # 处理窗口拖拽
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.press_pos = event.pos()
            self.draggable = True
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if self.draggable:
            new_pos = event.globalPos() - self.press_pos
            self.move(new_pos)
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.width(), self.height(), self.background_image)



