from PySide6.QtWidgets import QWidget

class main_win(QWidget):
    def __init__(self,parent_window):
        super().__init__()
        self.resize(800,600)
        self.parent = parent_window