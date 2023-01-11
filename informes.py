import os, var
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime


class Informes:
    def listClientes(self):
        try:
            var.report = canvas.Canvas('informes/listadoClientes.pdf')
            titulo = 'LISTADO CLIENTES'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['DNI', 'Nombre', 'Dirección', 'Municipio', 'Provincia']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(60, 700, str(items[0]))
            var.report.drawString(160, 700, str(items[1]))
            var.report.drawString(260, 700, str(items[2]))
            var.report.drawString(370, 700, str(items[3]))
            var.report.drawString(470, 700, str(items[4]))
            var.report.line(50, 695, 525, 695)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, nombre, direccion, municipio, provincia from clientes order by dni')
            var.report.setFont('Helvetica', size=8)
            if query.exec():
                i = 55
                j = 680
                while query.next():
                    if j < 80:
                        var.report.drawString(460, 90, 'Pagina siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(60, 700, str(items[0]))
                        var.report.drawString(160, 700, str(items[1]))
                        var.report.drawString(260, 700, str(items[2]))
                        var.report.drawString(370, 700, str(items[3]))
                        var.report.drawString(470, 700, str(items[4]))
                        var.report.line(50, 695, 525, 695)
                        i = 55
                        j = 680
                    var.report.setFont('Helvetica', size=8)
                    dni = str(query.value(0)[5:8])
                    var.report.drawString(i + 5, j, str('*****'+dni+'*'))
                    var.report.drawString(i + 105, j, str(query.value(1)))
                    var.report.drawString(i + 205, j, str(query.value(2)))
                    var.report.drawString(i + 315, j, str(query.value(3)))
                    var.report.drawString(i + 415, j, str(query.value(4)))
                    j = j - 20
            var.report.save()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Informe', 'informeClientes.pdf', '.pdf')
            if directorio:
                os.rename('informes/listadoClientes.pdf', directorio)
                QtWidgets.QMessageBox.information(None, 'Guardar Informe', 'Informe guardado correctamente')
            rootPath = '.\\informes'
            '''for file in os.listdir((rootPath)):
                if file.endswith(('Clientes.pdf')):
                    os.startfile('%s\%s' % (rootPath, file))'''
        except Exception as error:
            print('Error informes estado clientes' % str(error))

    def listAutos(self):
        try:
            var.report = canvas.Canvas('informes/listadoAutos.pdf')
            titulo = 'LISTADO VEHÍCULOS'
            Informes.pieInforme(titulo)
            Informes.topInforme(titulo)
            items = ['DNI', 'Matricula', 'Marca', 'Modelo', 'Motor']
            var.report.setFont('Helvetica-Bold', size=10)
            var.report.drawString(60, 700, str(items[0]))
            var.report.drawString(160, 700, str(items[1]))
            var.report.drawString(260, 700, str(items[2]))
            var.report.drawString(370, 700, str(items[3]))
            var.report.drawString(470, 700, str(items[4]))
            var.report.line(50, 695, 525, 695)
            query = QtSql.QSqlQuery()
            query.prepare('select dnicli, matricula, marca, modelo, motor from coches order by dnicli')
            var.report.setFont('Helvetica', size=8)
            if query.exec():
                i = 55
                j = 680
                while query.next():
                    if j < 80:
                        var.report.drawString(460, 90, 'Pagina siguiente...')
                        var.report.showPage()
                        Informes.topInforme(titulo)
                        Informes.pieInforme(titulo)
                        var.report.setFont('Helvetica-Bold', size=10)
                        var.report.drawString(60, 700, str(items[0]))
                        var.report.drawString(160, 700, str(items[1]))
                        var.report.drawString(260, 700, str(items[2]))
                        var.report.drawString(370, 700, str(items[3]))
                        var.report.drawString(470, 700, str(items[4]))
                        var.report.line(50, 695, 525, 695)
                        i = 55
                        j = 680
                    var.report.setFont('Helvetica', size=8)
                    dni = str(query.value(0)[5:8])
                    var.report.drawString(i + 5, j, str('*****'+dni+'*'))
                    var.report.drawString(i + 105, j, str(query.value(1)))
                    var.report.drawString(i + 205, j, str(query.value(2)))
                    var.report.drawString(i + 315, j, str(query.value(3)))
                    var.report.drawString(i + 415, j, str(query.value(4)))
                    j = j - 20
            var.report.save()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Informe', 'informeCoches.pdf', '.pdf')
            if directorio:
                os.rename('informes/listadoCoches.pdf', directorio)
                QtWidgets.QMessageBox.information(None, 'Guardar Informe', 'Informe guardado correctamente')
            '''rootPath = '.\\informes'
            for file in os.listdir((rootPath)):
                if file.endswith(('Autos.pdf')):
                    os.startfile('%s\%s' % (rootPath, file))'''
        except Exception as error:
            print('Error informes estado vehiculos' % str(error))

    def pieInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica-Oblique', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))

        except Exception as error:
            print('Error en pie informe de cualquier tipo: ', error)

    def topInforme(titulo):
        try:
            logo = '.\img\logo-taller.png'
            var.report.line(50, 800, 525, 800)
            var.report.setFont('Helvetica-Bold', size=14)
            var.report.drawString(55, 785, 'Taller Mecánico Teis')
            var.report.drawString(240, 720, titulo)
            var.report.line(50, 715, 525, 715)
            var.report.drawImage(logo, 430, 735, width=95, height=55)
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 770, 'CIF: A12345678')
            var.report.drawString(55, 760, 'Avda. Galicia - 101')
            var.report.drawString(55, 750, 'Vigo - 36216 - España')
            var.report.drawString(55, 740, 'Teléfono: 986 123 456')
            var.report.drawString(55, 730, 'e-mail: mitaller@mail.com')


        except Exception as error:
            print('Error en cabecera informe:', error)
