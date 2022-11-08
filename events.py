import sys, var, shutil, os
import zipfile
from datetime import date, datetime
from PyQt6 import QtWidgets

import conexion


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

    def abrirCalendar(self = None):
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
            #var.dlgabrir.show()
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            copia = (str(fecha)+'_backup.zip')
            #option = QtWidgets.QFileDialog
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia', copia, '.zip')

            if var.dlgabrir.accept and filename != '':
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia),str(directorio))
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
            filename= var.dlgabrir.getOpenFileName(None, 'Restaurar Copia Seguridad', '', '*.zip;;All Files')
            if var.dlgabrir.accept and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.dbconexion()
            conexion.Conexion.mostrarTabcarcli()

        except Exception as error:
            print('Error restaura backup', error)