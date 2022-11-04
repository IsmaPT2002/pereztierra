from PyQt6 import QtWidgets, QtSql
import var
from ventMain import *


class Conexion():
    def dbconexion(self=None):
        filedb = 'bbdd.sqlite'
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filedb)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se abre la base de datos', 'Conexión no establecida.\n',
                                           'Haga click para cerrar', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión establecida')
        return True

    def cargarProv(self=None):
        try:
            var.ui.cmbProcli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec():
                var.ui.cmbProcli.addItem('')
                while query.next():
                    var.ui.cmbProcli.addItem(query.value(0))

        except Exception as error:
            print('Error cargar provincias', error)

    def selMuni(self):
        try:
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProcli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select id from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where provincia_id = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbMunicli.addItem('')
                while query1.next():
                    var.ui.cmbMunicli.addItem(query1.value(0))

        except Exception as error:
            print('Error cargar municipios', error)

    @staticmethod
    def altaCli(newcli, newcar):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert or replace into clientes (dni, nombre, alta, direccion, provincia, municipio, pago) '
                          ' VALUES (:dni, :nombre, :alta, :direccion, :provincia, :municipio, :pago)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':nombre', str(newcli[1]))
            query.bindValue(':alta', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':municipio', str(newcli[5]))
            query.bindValue(':pago', str(newcli[6]))

            if query.exec():
                query1 = QtSql.QSqlQuery()
                query1.prepare('insert or replace into coches (matricula, dnicli, marca, modelo, motor) '
                               ' VALUES (:matricula, :dnicli, :marca, :modelo, :motor)')
                query1.bindValue(':matricula', str(newcar[0]))
                query1.bindValue(':dnicli', str(newcli[0]))
                query1.bindValue(':marca', str(newcar[1]))
                query1.bindValue(':modelo', str(newcar[2]))
                query1.bindValue(':motor', str(newcar[3]))

                if query1.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Cliente - Coche dado de Alta')
                    msg.exec()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText(query1.lastError().text())
                    msg.exec()
                Conexion.mostrarTabcarcli()

        except Exception as error:
            print('problemas conexion alta cliente', error)

    def mostrarTabcarcli(self =None):
        try:
            index=0
            query =QtSql.QSqlQuery()
            query.prepare('select matricula, dnicli, marca, modelo, motor from '
                          'coches order by marca, modelo')
            if query.exec():
                while query.next():
                    var.ui.tbClientes.setRowCount(index+1) #creamos la fila
                    var.ui.tbClientes.setItem(index,0,QtWidgets.QTableWidgetItem(str(query.value(1))))
                    var.ui.tbClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(0))))
                    var.ui.tbClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(2))))
                    var.ui.tbClientes.setItem(index,3,QtWidgets.QTableWidgetItem(str(query.value(3))))
                    var.ui.tbClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(query.value(4))))
                    var.ui.tbClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tbClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tbClientes.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    var.ui.tbClientes.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    index += 1



        except Exception as error:
            print('Problema mostrar listado coches clientes', error)