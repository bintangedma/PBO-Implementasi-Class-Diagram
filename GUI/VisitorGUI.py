from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QMessageBox, QApplication
import sys

from Class.Authority import Authority
from Class.JenKel import JenKel
#from Class.Employee import Employee
from db.Orm.VisitorOrm import VisitorOrm
from GUI.ReusableComponent.EditLineRC import EditLineRC
from GUI.ReusableComponent.QComboBoxRC import QComboBoxRC
from GUI.ReusableComponent.QFrameRC import QFrameRC
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QPushButtonRC2 import QPushButtonRC2


class VisitorView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VISITOR FORM.")
        self.setModal(True)
        self.resize(550, 350)

        #  >>>FONT CONFIGURE<<<
        self.font = QtGui.QFont()
        self.font.setFamily("Product Sans")
        self.font.setPointSize(12)
        self.font.setWeight(55)

        # >>> BASE SECTION <<<
        self.layoutUtama = QGridLayout()

        # >>> FIRST LAYOUT <<<
        framelayout1 = QFrameRC("white")
        framelayout1.setContentsMargins(25, 25, 25, 25)
        layout1 = QGridLayout(framelayout1)

        lbljudul = QLabelRC("Data Visitor", "rgb(125, 15, 15)")

        lblnoKtp = QLabelRC("\nNomor KTP\n", "black")
        lblnoKtp.setFont(self.font)
        self.txtnoKtp = EditLineRC("Input Nomor KTP anda")

        lbljeniskelamin = QLabelRC("\nJenis Kelamin\n", "grey")
        lbljeniskelamin.setFont(self.font)
        self.cmbjeniskelamin = QComboBoxRC()
        self.cmbjeniskelamin.addItems(
            ['Laki-laki', 'Perempuan'])
        self.pilJenisKelamin = [JenKel.Lakilaki, JenKel.Perempuan]

        lblnama = QLabelRC("\nNama\n", "black")
        lblnama.setFont(self.font)
        self.txtnama = EditLineRC("Input Nama")

        lblTL = QLabelRC("\n\nTanggal Lahir\n", "grey")
        lblTL.setFont(self.font)
        self.txtTL = EditLineRC("")

        lblalamat = QLabelRC("\n\nAlamat\n", "black")
        lblalamat.setFont(self.font)
        self.txtalamat = EditLineRC("Input Alamat")

        # >>> ADD DATA <<<
        self.btnTambah = QPushButtonRC2("Tambah Data", "Assets/img/button.png")
        self.btnTambah.setStyleSheet("background-color : rgb(125, 15, 15);\n"
                                     "border : none;\n"
                                     "border-radius : 25px;\n"
                                     "height : 50%;\n"
                                     "color : white;\n")
        self.btnTambah.setIconSize(QtCore.QSize(60, 35))

        self.btnMainMenu = QPushButtonRC2("Main Menu", "Assets/img/back.png")
        self.btnMainMenu.setStyleSheet("background-color : rgb(125, 15, 15);\n"
                                       "border : none;\n"
                                       "border-radius : 25px;\n"
                                       "height : 50%;\n"
                                       "color : white;\n")
        self.btnMainMenu.setIconSize(QtCore.QSize(60, 35))

        # >>> EVENT SECTION <<<
        self.btnTambah.clicked.connect(lambda: self.insertData())
        self.btnMainMenu.clicked.connect(lambda: self.switchMainMenu())

        # >>> LAYOUT SECTION <<<
        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignVCenter)
        self.layoutUtama.addWidget(self.btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)
        self.layoutUtama.addWidget(self.btnMainMenu, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignLeft)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblnama, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtnama, 2, 0, 2, 3)
        layout1.addWidget(lblTL, 4, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtTL, 5, 0, 2, 3)
        layout1.addWidget(lblalamat, 7, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtalamat, 8, 0, 2, 3)
        layout1.addWidget(lblnoKtp, 1, 5, 1, 3)
        layout1.addWidget(self.txtnoKtp, 2, 5, 2, 3)
        layout1.addWidget(lbljeniskelamin, 4, 5, 1, 3)
        layout1.addWidget(self.cmbjeniskelamin, 5, 5, 2, 3)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.id_visitor = self.txtnama.text()+self.txtTL.text()
        self.nama = self.txtnama.text()
        self.jk = self.pilJenisKelamin[self.cmbjeniskelamin.currentIndex()]
        self.alamat = self.txtalamat.text()
        self.no_KTP = self.txtnoKtp.text()
        self.tanggal_lahir = self.txtTL.text()
        visitor = VisitorOrm(self.id_visitor, self.nama, self.jk, self.alamat, self.no_KTP , self.tanggal_lahir)
        try:
            VisitorOrm.insertVisitor(visitor)
        except Exception as e:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Something Wrong", e)
            msg.setWindowTitle("GAGAL")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Data Berhasil Di Input!")
            msg.setWindowTitle("BERHASIL")
            msg.exec_()
            self.clear()

    def switchMainMenu(self):
        self.close()

    def clear(self):
        self.txtname.setText("")
        self.txtid.setText("")
        self.cmbauthority.setCurrentIndex(0)
        self.cmbjeniskelamin.setCurrentIndex(0)
        self.txtname.setFocus()

#app = QApplication(sys.argv)
#emp = VisitorView()
#emp.show()
#sys.exit(app.exec_())
