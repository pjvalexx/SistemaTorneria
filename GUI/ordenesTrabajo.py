from PyQt6 import uic
from conexion import Conexion 
from GUI.formularioOrden import FormularioOrden
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem

class OrdenesTrabajoWindow():
    def __init__(self):
        self.ordenesTrabajoWindow = uic.loadUi("GUI/ordenesTrabajo.ui")
        #self.initGUI()
        self.ordenesTrabajoWindow.show()
        self.ordenesTrabajoWindow.nuevaOrdenBoton.clicked.connect(self.abrir_ventana_formulario_orden)
        self.ordenesTrabajoWindow.irAlMenu.clicked.connect(self.ir_al_menu_principal)
        self.cargar_ordenes()
        
    def abrir_ventana_formulario_orden(self):
        # self.ordenesTrabajoWindow.hide()
        self.formulario_orden = FormularioOrden()
        
    
    def ir_al_menu_principal(self):
        self.ordenesTrabajoWindow.hide()


    def cargar_ordenes(self):
        conexion = Conexion()
        try:
            # Consultar las órdenes de trabajo desde la base de datos
            cur = conexion.con.cursor()
            cur.execute("SELECT * FROM orden_trabajo")
            ordenes = cur.fetchall()

            # Agregar cada orden a la tabla
            for orden in ordenes:
                row_position = self.ordenesTrabajoWindow.tableWidgetOrdenes.rowCount()
                self.ordenesTrabajoWindow.tableWidgetOrdenes.insertRow(row_position)
                self.ordenesTrabajoWindow.tableWidgetOrdenes.verticalHeader().setVisible(False)
                
                
                # Agregar datos a las celdas de la tabla
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 0, QTableWidgetItem(str(orden[0])))  # ID
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 1, QTableWidgetItem(orden[1]))  # Nombre
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 2, QTableWidgetItem(orden[2]))  # Teléfono
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 3, QTableWidgetItem(orden[3]))  # direccion
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 4, QTableWidgetItem(orden[4]))  # Tipo Servicio
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 5, QTableWidgetItem(orden[5]))  # Descripcion
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 6, QTableWidgetItem(orden[6]))  # dObservacion
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 7, QTableWidgetItem(orden[7]))  # Materiales
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 8, QTableWidgetItem(orden[8]))  # Fecha Entrega
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 9, QTableWidgetItem(f"{orden[9]:.2f}"))  # Monto
                self.ordenesTrabajoWindow.tableWidgetOrdenes.setItem(row_position, 10, QTableWidgetItem(orden[10]))  # Fecha Creacion

                
        except Exception as ex:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("error")
            msg_box.setText("no se pudo cargar")
            msg_box.exec()
        finally:
            conexion.cerrar_conexion()