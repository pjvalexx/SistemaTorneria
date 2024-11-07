from PyQt6 import uic
from GUI.ordenesTrabajo import OrdenesTrabajoWindow
from GUI.inventario import InventarioWindow

class MainWindow():
    def __init__(self):
        self.main = uic.loadUi("GUI/main.ui")
        #self.initGUI()
        self.main.show()
        self.main.ordenesTrabajoBoton.clicked.connect(self.abrir_ventana_ordenes_trabajo)
        self.main.inventarioBoton.clicked.connect(self.abrir_ventana_inventario)
        self.main.cerrarSesionBoton.clicked.connect(self.cerrar_sesion)
        
    def abrir_ventana_ordenes_trabajo(self):
        # self.main.hide()
        self.ordenes_trabajo_window = OrdenesTrabajoWindow()

    def abrir_ventana_inventario(self):
        # self.main.hide()
        self.inventario_window = InventarioWindow()
    
    def cerrar_sesion(self):
        self.main.hide()