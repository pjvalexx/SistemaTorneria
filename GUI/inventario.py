from PyQt6 import uic


class InventarioWindow():
    def __init__(self):
        self.inventarioWindow = uic.loadUi("GUI/inventario.ui")
        #self.initGUI()
        self.inventarioWindow.show()
        self.inventarioWindow.irAlMenu.clicked.connect(self.ir_al_menu_principal)
    
    def ir_al_menu_principal(self):
        self.inventarioWindow.hide()