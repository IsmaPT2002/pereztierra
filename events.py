import sys, var, shutil, os
import zipfile, xlwt
from datetime import date, datetime
import xlrd
from PyQt6 import QtWidgets, QtSql

import clientes
import conexion
from main import DialogExportar, DialogAbrir


class Eventos:
    def Salir(self):
        try:
            var.avisosalir.show()
            if var.avisosalir.exec():
                sys.exit()
            else:
                var.avisosalir.hide()
        except Exception as error:
            print("Error en función salir %s", str(error))

    def abrirCalendar(self=None):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error abrir calendario: ', error)

    def resizeTablacarcli(self):
        try:
            header = var.ui.tbClientes.horizontalHeader()
            for i in range(5):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
                if i == 0 or i == 1:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        except Exception as error:
            print('Error dimensionar tabla coches: ', error)

    def creaBackup(self):
        try:
            # var.dlgabrir.show()
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = (str(fecha) + '_backup.zip')
            # option = QtWidgets.QFileDialog
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', copia, '.zip')

            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad Creada')
                msg.exec()

        except Exception as error:
            print('Error crear backup', error)

    def restauraBackup(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia Seguridad', '', '*.zip;;All Files (*)')
            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.dbconexion()
            conexion.Conexion.mostrarTabcarcli()

        except Exception as error:
            print('Error restaura backup', error)

    def exportarDatos(self):
        try:

            dlgExportar = DialogExportar()
            if dlgExportar.exec():
                if not dlgExportar.ui.checkboxCoches.isChecked() and not dlgExportar.ui.checkboxClientes.isChecked():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText("Debes seleccionar al menos una opción")
                    msg.exec()
                    self.exportarDatos()
                    return
                dialogo_abrir = DialogAbrir()
                directorio = dialogo_abrir.getSaveFileName(self, "Exportar a Excel", "",
                                                           "Excel (*.xls)")
                if directorio[0]:
                    self.servicioBackup.exportar_excel(directorio[0],
                                                       dlgExportar.ui.checkboxClientes.isChecked(),
                                                       dlgExportar.ui.checkboxCoches.isChecked())
                    msg = QtWidgets.QMessageBox()
                    msg.setModal(True)
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Se ha exportado a Excel correctamente")
                    msg.exec()


            '''
            var.avisoexportar.show()
            if var.ui.chkClientes.isChecked():
                fecha = datetime.today()
                fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
                file = (str(fecha) + '_Clientes.xls')
                directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Datos', file, '.xls')
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'DNI')
                sheet1.write(0, 1, 'Nombre')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Direccion')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Forma de pago')
                fila = 1
                query = QtSql.QSqlQuery()
                query.prepare('select * from clientes order by dni')
                if query.exec():
                    while query.next():
                        sheet1.write(fila, 0, str(query.value(0)))
                        sheet1.write(fila, 1, str(query.value(1)))
                        sheet1.write(fila, 2, str(query.value(2)))
                        sheet1.write(fila, 3, str(query.value(3)))
                        sheet1.write(fila, 4, str(query.value(4)))
                        sheet1.write(fila, 5, str(query.value(5)))
                        sheet1.write(fila, 6, str(query.value(6)))
                        fila += 1
                if (wb.save(directorio)):
                    msg = QtWidgets.QMessageBox()
                    msg.setModal(True)
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Exportacion de Clientes Realizada')
                    msg.exec()
        except Exception as error:
            print("Error exportar datos", error)

    def importarDatos(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Importar Datos', '', '*.xls;;All Files (*)')
            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                new = []
                for i in range(filas):
                    if i==0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            new.append(datos.cell_value(i,j))
                            if clientes.Clientes.validarDNI(str(new[0])):
                                conexion.Conexion.altaExcelCoche(new)
                conexion.Conexion.mostrarTabcarcli(self)
                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importacion de Datos Realizada')
                msg.exec()
                '''
        except Exception as error:
            print("Error importar datos", error)