from PyQt6 import uic
from conexion import Conexion 
from PyQt6.QtWidgets import QWidget, QMessageBox

class FormularioOrden():
    def __init__(self):
        self.formularioOrden = uic.loadUi("GUI/formularioOrden.ui")
        #self.initGUI()
        self.formularioOrden.show()
        self.formularioOrden.crearOrdenBoton.clicked.connect(self.crear_orden)
        
    def crear_orden(self):
        # Obtener los valores de los campos de entrada del formulario
        nombre = self.formularioOrden.inputNombre.text()
        telefono = self.formularioOrden.inputTelefono.text()
        direccion = self.formularioOrden.inputDireccion.text()
        tipo_servicio = self.formularioOrden.inputTipoServicio.text()
        descripcion_servicio = self.formularioOrden.inputDescripcion.text()
        observaciones = self.formularioOrden.inputObservaciones.text()
        fecha_entrega = self.formularioOrden.inputFechaEntrega.date().toString("yyyy-MM-dd")
        materiales = self.formularioOrden.inputMateriales.text()
        monto = float(self.formularioOrden.inputMonto.text()) if self.formularioOrden.inputMonto.text() else 0.0
    
        conexion = Conexion()
        conexion.insertar_orden(nombre, telefono, direccion, tipo_servicio, descripcion_servicio,
                                    observaciones, fecha_entrega, materiales, monto)
        conexion.cerrar_conexion()
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Éxito")
        msg_box.setText("Orden de trabajo creada exitosamente.")
        msg_box.exec()
        self.limpiar_campos()
        self.formularioOrden.hide()
        
    def limpiar_campos(self):
        # Limpiar los campos del formulario
        self.formularioOrden.inputNombre.clear()
        self.formularioOrden.inputTelefono.clear()
        self.formularioOrden.inputDireccion.clear()