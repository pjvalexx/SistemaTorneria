from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

from GUI.main import MainWindow
from data.usuario import UsuarioData
from model.usuario import Usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi("GUI/login.ui")
        self.initGUI()
        self.login.lblError.setText("")
        self.login.show()
        
    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblError.setText("Ingrese un usuario valido")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text()) < 3:
            self.login.lblError.setText("Ingrese una contraseña valida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblError.setText("")
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text(),)
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
               self.main = MainWindow()
               self.login.hide()
            else:
                self.login.lblError.setText("datos incorrectos")

    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)
