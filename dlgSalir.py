# Form implementation generated from reading ui file 'dlgSalir.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgSalir(object):
    def setupUi(self, dlgSalir):
        dlgSalir.setObjectName("dlgSalir")
        dlgSalir.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        dlgSalir.resize(300, 200)
        dlgSalir.setMinimumSize(QtCore.QSize(300, 200))
        dlgSalir.setMaximumSize(QtCore.QSize(300, 200))
        dlgSalir.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgSalir)
        self.buttonBox.setGeometry(QtCore.QRect(70, 120, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblImgaviso = QtWidgets.QLabel(dlgSalir)
        self.lblImgaviso.setGeometry(QtCore.QRect(120, 20, 61, 61))
        self.lblImgaviso.setText("")
        self.lblImgaviso.setPixmap(QtGui.QPixmap("img/advertencia.png"))
        self.lblImgaviso.setScaledContents(True)
        self.lblImgaviso.setObjectName("lblImgaviso")
        self.lblSalir = QtWidgets.QLabel(dlgSalir)
        self.lblSalir.setGeometry(QtCore.QRect(110, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblSalir.setFont(font)
        self.lblSalir.setObjectName("lblSalir")

        self.retranslateUi(dlgSalir)
        self.buttonBox.accepted.connect(dlgSalir.accept) # type: ignore
        self.buttonBox.rejected.connect(dlgSalir.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Salir"))
        self.lblSalir.setText(_translate("dlgSalir", "Desea salir?"))
