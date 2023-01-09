import os, var
from reportlab.pdfgen import canvas
from datetime import datetime

class Informes:
    def listClientes(self):
        try:
            var.report = canvas.Canvas("informes/listadoClientes.pdf")
            titulo = "LISTADO CLIENTES"
            var.report.drawString(100, 750, str(titulo))
            Informes.pieInforme(titulo)
            var.report.save()
            rootPath ='.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith("Clientes.pdf"):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print("Error informes estado clientes" %str(error))

    def listAutos(self):
        try:
            var.report = canvas.Canvas("informes/listadoAutos.pdf")
            titulo = "LISTADO VEHICULOS"
            var.report.drawString(100, 750, str(titulo))
            Informes.pieInforme(titulo)
            var.report.save()
            rootPath ='.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith("Autos.pdf"):
                    os.startfile('%s\%s' % (rootPath, file))
        except Exception as error:
            print("Error informes estado vehiculos" %str(error))
    def pieInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime("%d-%m-%Y %H:%M:%S")
            var.report.setFont("Helvetica-Oblique", size = 7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, ("Página %s" % var.report.getPageNumber()))

        except Exception as error:
            print("Error en pie de informe de cualquier tipo", error)