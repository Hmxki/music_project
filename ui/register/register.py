from PySide6.QtGui import QIcon, QPixmap, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton
from ui.register.generate_account import generate_nonzero_start_account

class register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("注册")
        self.resize(400, 300)
        self.setui()

    def setui(self):
        pix = QPixmap("./source/icon/register.png")
        icon = QIcon(pix)
        self.setWindowIcon(icon)
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        # 注册界面添加账号，密码，去确认按钮等控件
        information = '请记住生成的账号，并设置密码！'
        self.information = QLabel(self)
        self.information.setText(information)
        self.information.setFixedSize(200,30)
        self.information.setAlignment(Qt.AlignCenter)
        information_layout = QHBoxLayout()
        information_layout.addWidget(self.information)

        self.count_label = QLabel('账号',self)
        self.count_lineedit = QLineEdit(self)

        self.password_label = QLabel('密码',self)
        self.password_lineedit = QLineEdit(self)

        self.confirm_button = QPushButton('确认',self)
        self.confirm_button.setFixedSize(60,30)

        confirm_layout = QHBoxLayout()
        confirm_layout.addStretch()  # 在按钮之前添加弹簧，将按钮居中对齐
        confirm_layout.addWidget(self.confirm_button)
        confirm_layout.addStretch()  # 在按钮之后添加弹簧，将按钮居中对齐

        self.password_lineedit.setEchoMode(QLineEdit.Password)

        count_layout = QHBoxLayout()
        password_layout = QHBoxLayout()
        count_layout.addWidget(self.count_label)
        count_layout.addWidget(self.count_lineedit)
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_lineedit)

        count_layout.setSpacing(15)
        password_layout.setSpacing(15)

        v_layout = QVBoxLayout(self)
        v_layout.addLayout(information_layout)
        v_layout.addLayout(count_layout)
        v_layout.addLayout(password_layout)
        v_layout.addStretch()
        v_layout.addLayout(confirm_layout)
        v_layout.setContentsMargins(100, 80, 100, 50)
        v_layout.setSpacing(20)

        # 在账号一栏中显示生成的账号
        generate_count = generate_nonzero_start_account(10)
        self.count_lineedit.setText(generate_count)




