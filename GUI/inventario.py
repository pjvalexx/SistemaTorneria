from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QInputDialog, QTableWidget
from conexion import Conexion

class InventarioWindow():
    def __init__(self):
        # Cargar la interfaz del inventario
        self.inventarioWindow = uic.loadUi("GUI/inventario.ui")
        self.inventarioWindow.show()

        # Conectar botones a sus funciones correspondientes
        self.inventarioWindow.nuevo_item.clicked.connect(self.agregar_item)
        self.inventarioWindow.botonModificarStock.clicked.connect(self.modificar_stock)
        self.inventarioWindow.irAlMenu.clicked.connect(self.ir_al_menu_principal)

        # Cargar el inventario inicial
        self.cargar_inventario()

    def cargar_inventario(self):
        conexion = Conexion()
        try:
            # Consultar el inventario
            cur = conexion.con.cursor()
            cur.execute("SELECT * FROM inventario")
            items = cur.fetchall()

            # Limpiar y llenar la tabla
            self.inventarioWindow.tableWidgetInventario.setRowCount(0)
            self.inventarioWindow.tableWidgetInventario.verticalHeader().setVisible(False)
            
          # Configurar para seleccionar toda la fila
            self.inventarioWindow.tableWidgetInventario.setSelectionBehavior(
                QTableWidget.SelectionBehavior.SelectRows
            )

            
            for item in items:
                row_position = self.inventarioWindow.tableWidgetInventario.rowCount()
                self.inventarioWindow.tableWidgetInventario.insertRow(row_position)

                # Llenar cada columna de la tabla
                for col, data in enumerate(item):
                    self.inventarioWindow.tableWidgetInventario.setItem(row_position, col, QTableWidgetItem(str(data)))
            
            # Ajustar tamaño de las columnas automáticamente al contenido
            self.inventarioWindow.tableWidgetInventario.resizeColumnsToContents()

            # Ajustar tamaño de las filas automáticamente al contenido
            self.inventarioWindow.tableWidgetInventario.resizeRowsToContents()
            
                    
        except Exception as ex:
            QMessageBox.critical(self.inventarioWindow, "Error", f"No se pudo cargar el inventario: {ex}")
        finally:
            conexion.cerrar_conexion()

    def agregar_item(self):
        
        # Solicitar el nombre del ítem
        nombre, ok = QInputDialog.getText(None, "Agregar Ítem", "Nombre del ítem:")
        if not ok or not nombre:
            return  # Cancelado o vacío
        
        # Solicitar la cantidad inicial
        cantidad, ok = QInputDialog.getInt(None, "Agregar Ítem", "Cantidad inicial:", 1, 0)
        if not ok:
            return  # Cancelado
        conexion = Conexion()
        # Insertar el ítem en la base de datos
        try:
            sql_insert = """
                INSERT INTO inventario (nombre, cantidad)
                VALUES (?, ?)
            """
            cursor = conexion.con.cursor()
            cursor.execute(sql_insert, (nombre, cantidad))
            conexion.con.commit()
            cursor.close()
            
            # Mostrar mensaje de éxito
            QMessageBox.information(None, "Éxito", "Ítem añadido al inventario.")
            self.cargar_inventario()
        except Exception as ex:
            QMessageBox.warning(None, "Error", f"No se pudo añadir el ítem: {ex}")



    def modificar_stock(self):
        # Asegúrate de que haya un ítem seleccionado
        selected_row = self.inventarioWindow.tableWidgetInventario.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self.inventarioWindow, "Advertencia", "Por favor selecciona un ítem para modificar.")
            return

        # Obtener el ID del ítem seleccionado
        item_id = self.inventarioWindow.tableWidgetInventario.item(selected_row, 0).text()
        nombre_item = self.inventarioWindow.tableWidgetInventario.item(selected_row, 1).text()  # Para mostrar en el diálogo

        # Pedir al usuario el nuevo stock usando un cuadro de entrada
        nuevo_stock, ok = QInputDialog.getInt(
            self.inventarioWindow,
            "Modificar Stock",
            f"Ingresa el nuevo stock para '{nombre_item}':",
            min=0  # Evitar números negativos
        )

        # Si el usuario cancela, salir de la función
        if not ok:
            return

        # Actualizar el stock en la base de datos
        conexion = Conexion()
        try:
            sql_update = "UPDATE inventario SET cantidad = ? WHERE id = ?"
            cur = conexion.con.cursor()
            cur.execute(sql_update, (nuevo_stock, item_id))
            conexion.con.commit()
            QMessageBox.information(self.inventarioWindow, "Éxito", "Stock actualizado correctamente.")
            
            # Recargar la tabla para reflejar los cambios
            self.cargar_inventario()
            
        except Exception as ex:
            QMessageBox.critical(self.inventarioWindow, "Error", f"No se pudo modificar el stock: {ex}")
        finally:
            conexion.cerrar_conexion()
        
    def ir_al_menu_principal(self):
        self.inventarioWindow.hide()