from PyQt6 import QtWidgets

import conexion
import var


class Clientes():
    def validarDNI(dni):
        '''
        Módulo para la validación del DNI
        :return: booleano
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False
        except Exception as error:
            print('Error validad dni: ', error)

    def mostraValidodni(self=None):
        try:
            dni = var.ui.txtDni.text()
            if Clientes.validarDNI(dni):
                var.ui.lblValidardni.setStyleSheet('color: green;')
                var.ui.lblValidardni.setText('V')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: white;')
            else:
                var.ui.lblValidardni.setStyleSheet('color: red;')
                var.ui.lblValidardni.setText('X')
                var.ui.txtDni.setText(dni.upper())
                var.ui.txtDni.setStyleSheet('background-color: pink;')

        except Exception as error:
            print('Error mostrar marcado validez dni:', error)

    def selMotor(self):
        try:
            var.motor = (var.ui.rbtDiesel, var.ui.rbtGasolina, var.ui.rbtHibrido, var.ui.rbtElectrico)
            for i in var.motor:
                i.toggled.connect(Clientes.selMotor)
        except Exception as error:
            print('Error selección motor:', error)

    def checkMotor(self=None):
        try:
            if var.ui.rbtGasolina.isChecked():
                motor = 'Gasolina'
            elif var.ui.rbtDiesel.isChecked():
                motor = 'Diesel'
            elif var.ui.rbtHibrido.isChecked():
                motor = 'Hibrido'
            elif var.ui.rbtElectrico.isChecked():
                motor = 'Electrico'
            else:
                pass
            return motor
        except Exception as error:
            print('Error selección motor:', error)

    def guardaCli(self):
        try:
            newcli = []
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtFechaltacli, var.ui.txtDircli]
            for i in cliente:
                newcli.append(i.text())
            prov = var.ui.cmbProcli.currentText()
            newcli.append(prov)
            muni = var.ui.cmbMunicli.currentText()
            newcli.append(muni)
            pagos = []
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkFactura.isChecked():
                pagos.append('Factura')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transferencia')
            pagos = set(pagos) #evita duplicados
            newcli.append('; '.join(pagos))
            print(newcli)
            newcar = []
            car = [var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]
            for i in car:
                newcar.append(i.text())
            motor = Clientes.checkMotor()
            newcar.append(motor)
            print(newcar)
            conexion.Conexion.altaCli(newcli, newcar)
            '''
            row = 0
            column = 0
            var.ui.tbClientes.insertRow(row)
            for registro in newcli:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.tbClientes.setItem(row, column, cell)
                column += 1
            '''
        except Exception as error:
            print('Error en carga cliente: ', error)

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaltacli.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en carga cliente: ', error)

    def mayusculaPalabra(self=None):
        var.ui.txtMarca.setText(var.ui.txtMarca.text().title())
        var.ui.txtModelo.setText(var.ui.txtModelo.text().title())
        var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
        var.ui.txtDircli.setText(var.ui.txtDircli.text().title())
        var.ui.txtDni.setText(var.ui.txtDni.text().title())
        var.ui.txtCar.setText(var.ui.txtCar.text().upper())

    def limpiaCli(self=None):
        try:
            cliente = [var.ui.txtDni, var.ui.txtNombre, var.ui.txtDircli, var.ui.txtFechaltacli, var.ui.txtCar,
                       var.ui.txtMarca, var.ui.txtModelo]
            for i in cliente:
                i.setText('')
            var.ui.cmbProcli.setCurrentText('')
            var.ui.cmbMunicli.setCurrentText('')
            checks = [var.ui.chkEfectivo, var.ui.chkFactura, var.ui.chkTrans]
            for i in checks:
                i.setChecked(False)
            conexion.Conexion.cargarProv(self)
        except Exception as error:
            print('Error limpiar cliente: ', error)

    def cargaCliente(self):
        try:
            Clientes.limpiaCli()
            fila = var.ui.tbClientes.selectedItems()
            row = [dato.text() for dato in fila]
            datos = [var.ui.txtDni, var.ui.txtCar, var.ui.txtMarca, var.ui.txtModelo]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            if row[4] == 'Gasolina':
                var.ui.rbtGasolina.setChecked(True)
            elif row[4] == 'Diesel':
                var.ui.rbtDiesel.setChecked(True)
            elif row[4] == 'Hibrido':
                var.ui.rbtHibrido.setChecked(True)
            elif row[4] == 'Electrico':
                var.ui.rbtElectrico.setChecked(True)
            registro = conexion.Conexion.oneCli(row[0])
            print(registro)
            var.ui.txtNombre.setText(registro[1])
            var.ui.txtFechaltacli.setText(registro[2])
            var.ui.txtDircli.setText(registro[3])
            var.ui.cmbProcli.setCurrentText(registro[4])
            var.ui.cmbMunicli.setCurrentText(registro[5])
            if registro[5] == 'Efectivo':
                var.ui.chkEfectivo.setChecked(True)
            elif registro[5] == 'Factura':
                var.ui.chkFactura.setChecked(True)
            elif registro[5] == 'Transferencia':
                var.ui.chkTrans.setChecked(True)

        except Exception as error:
            print('Error carga cliente', error)

    def borraCli(self):
        try:
            dni = var.ui.txtDni.text()
            conexion.Conexion.borraCli(dni)
            conexion.Conexion.mostrarTabcarcli(self)

        except Exception as error:
            print('Error baja Cliente y sus coches', error)
