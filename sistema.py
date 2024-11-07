from GUI.login import Login
from PyQt6.QtWidgets import QApplication

class Sistema():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
        
        