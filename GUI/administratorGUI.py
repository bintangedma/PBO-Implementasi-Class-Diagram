from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QMessageBox, QApplication
import sys

#from Class.Authority import Authority
from Class.User import User
from db.Orm.AdministratorOrm import AdministratorOrm
from GUI.ReusableComponent.EditLineRC import EditLineRC
from GUI.ReusableComponent.QComboBoxRC import QComboBoxRC
from GUI.ReusableComponent.QFrameRC import QFrameRC
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QPushButtonRC2 import QPushButtonRC2


class AdminView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADMIN FORM.")
        self.setModal(True)
        self.resize(550, 350)

        # >>>> FONT CONFIGURE <<<<
        self.font = QtGui.QFont()
        self.font.setFamily("Product Sans")
        self.font.setPointSize(12)
        self.font.setWeight(55)

        # >>>> BASE SECTION <<<<
        self.layoutUtama = QGridLayout()

        # >>>> FIRST LAYOUT <<<<
        framelayout1 = QFrameRC("white")
        framelayout1.setContentsMargins(25, 25, 25, 25)
        layout1 = QGridLayout(framelayout1)

        lbljudul = QLabelRC("Data Admin", "rgb(125, 15, 15)")

        lblnama = QLabelRC("\nNama\n", "grey")
        lblnama.setFont(self.font)
        self.txtnama = EditLineRC("")

        lblkode = QLabelRC("\n\nKode\n", "grey")
        lblkode.setFont(self.font)
        self.txtkode = EditLineRC("")

        # >>>> ADD DATA <<<<
        self.btnTambah = QPushButtonRC2("", "Assets/img/button.png")
        self.btnTambah.setStyleSheet("background-color : rgb(125, 15, 15);\n"
                                     "border : none;\n"
                                     "border-radius : 25px;\n"
                                     "height : 80%;\n"
                                     "color : white;\n")
        self.btnTambah.setIconSize(QtCore.QSize(75, 54))

        # >>>> EVENT SECTION <<<<
        self.btnTambah.clicked.connect(lambda: self.insertData())

        # >>>> LAYOUT SECTION <<<<
        self.layoutUtama.addWidget(framelayout1, 0, 0, 1, 9, Qt.AlignVCenter)
        self.layoutUtama.addWidget(self.btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblnama, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtnama, 2, 0, 2, 3)
        layout1.addWidget(lblkode, 4, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.txtkode, 5, 0, 2, 3)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.nama = self.txtnama.text()
        self.kode = self.txtkode.text()
        try:
            AdministratorOrm.insertAdmin(admin)
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

    def clear(self):
        self.txtnama.setText("")
        self.txtkode.setText("")
        self.txtnama.setFocus()

app = QApplication(sys.argv)
admin = AdminView()
admin.show()
sys.exit(app.exec_())
