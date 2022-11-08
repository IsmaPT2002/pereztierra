import conexion
from ventMain import *
from dlgSalir import *
from dlgCalendar import *
import sys,var,events,clientes
from datetime import *

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_dlgCalendar()
        var.dlgcalendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(ano, mes, dia))
        var.dlgcalendar.Calendar.clicked.connect(clientes.Clientes.cargaFecha)

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_dlgSalir()
        var.avisosalir.setupUi(self)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_ventMain()
        var.ui.setupUi(self)
        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        print(var.dlgcalendar.windowTitle())
        var.dlgabrir = FileDialogAbrir()

        '''
        Listados de eventos de menubar y menufile
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionSalirbar.triggered.connect(events.Eventos.Salir)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(events.Eventos.creaBackup)
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(events.Eventos.restauraBackup)

        '''
        Listados de eventos de menubar y menufile
        '''

        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mostraValidodni)
        var.ui.btnGuardacli.clicked.connect(clientes.Clientes.guardaCli)
        var.ui.btnFechaltacli.clicked.connect(events.Eventos.abrirCalendar)
        var.ui.btnLimpiacli.clicked.connect(clientes.Clientes.limpiaCli)

        var.ui.txtMarca.editingFinished.connect(clientes.Clientes.mayusculaPalabra)
        var.ui.txtModelo.editingFinished.connect(clientes.Clientes.mayusculaPalabra)
        var.ui.txtNombre.editingFinished.connect(clientes.Clientes.mayusculaPalabra)
        var.ui.txtDircli.editingFinished.connect(clientes.Clientes.mayusculaPalabra)
        var.ui.txtDni.editingFinished.connect(clientes.Clientes.mayusculaPalabra)
        var.ui.txtCar.editingFinished.connect(clientes.Clientes.mayusculaPalabra)

        '''
        Llamadas a funciones
        '''
        conexion.Conexion.dbconexion()
        conexion.Conexion.cargarProv()

        '''
        Llamadas a eventos de combobox
        '''
        conexion.Conexion.cargarProv()
        var.ui.cmbProcli.currentIndexChanged.connect(conexion.Conexion.selMuni)
        conexion.Conexion.mostrarTabcarcli(self)
        events.Eventos.resizeTablacarcli(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
