from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3

class ReportePDF:
    def __init__(self):
        self.conn = sqlite3.connect("sistema.db")
        self.cur = self.conn.cursor()

    def generar_reporte(self):
        # Crear un PDF
        archivo_pdf = "reporte_ordenes_trabajo.pdf"
        c = canvas.Canvas(archivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 10)

        # Título
        c.drawString(100, 750, "Reporte de Órdenes de Trabajo")
        
        # Consultar las órdenes de trabajo
        self.cur.execute("SELECT * FROM orden_trabajo")
        ordenes = self.cur.fetchall()

        # Posición inicial para el contenido
        y = 730

        # Añadir encabezados de columna
        c.drawString(100, y, "ID")
        c.drawString(150, y, "Nombre")
        c.drawString(250, y, "Telefono")
        c.drawString(350, y, "Tipo de Servicio")
        c.drawString(450, y, "Monto")
        y -= 15

        # Agregar las órdenes al PDF
        for orden in ordenes:
            c.drawString(100, y, str(orden[0]))  # ID
            c.drawString(150, y, orden[1])       # Nombre
            c.drawString(250, y, orden[2])       # Teléfono
            c.drawString(350, y, orden[4])       # Tipo de servicio
            c.drawString(450, y, str(orden[9]))  # Monto
            y -= 15

            # Si hay más de una página, creamos una nueva página
            if y < 100:
                c.showPage()  # Nueva página
                c.setFont("Helvetica", 10)
                y = 750  # Restablecemos la posición

        # Guardar el PDF
        c.save()
        print(f"Reporte guardado como {archivo_pdf}")

    def cerrar_conexion(self):
        self.conn.close()

# Crear un reporte
reporte = ReportePDF()
reporte.generar_reporte()
reporte.cerrar_conexion()
