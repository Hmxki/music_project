import sys
from PySide6.QtWidgets import QApplication
from ui.login.login import Login_Window
from ui.login.password_verify import hash_password




if __name__=="__main__":
    app = QApplication(sys.argv)
    login_window = Login_Window()
    login_window.show()
    sys.exit(app.exec())
