from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog, QGridLayout, QMessageBox, QApplication
import sys

from Class.Authority import Authority
from Class.JenKel import JenKel
from Class.Emptype import Emptype
from Class.RoomCode import RoomCode
from Class.RoomNumber import RoomNumber
#from Class.Employee import Employee
from db.Orm.RoomOrm import RoomOrm
from GUI.ReusableComponent.EditLineRC import EditLineRC
from GUI.ReusableComponent.QComboBoxRC import QComboBoxRC
from GUI.ReusableComponent.QFrameRC import QFrameRC
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QPushButtonRC2 import QPushButtonRC2


class BookView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BOOK A ROOM")
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

        lbljudul = QLabelRC("Pesan ruangan", "rgb(125, 15, 15)")

        lblnomorRuangan = QLabelRC("\nNomor Ruangan\n", "black")
        lblnomorRuangan.setFont(self.font)
        self.cmbnomorRuangan = QComboBoxRC()
        self.cmbnomorRuangan.addItems(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'])
        self.pilnomorRuangan = [RoomNumber.first, RoomNumber.second, RoomNumber.third, RoomNumber.fourth, RoomNumber.fifth,
                                RoomNumber.sixth, RoomNumber.seventh, RoomNumber.eighth, RoomNumber.nineth, RoomNumber.tenth]
        
        lbltipeRuangan = QLabelRC("\nTipe Ruangan\n", "black")
        lbltipeRuangan.setFont(self.font)
        self.cmbtipeRuangan = QComboBoxRC()
        self.cmbtipeRuangan.addItems(
            ['Normal', 'VIP', 'VVIP'])
        self.piltipeRuangan = [RoomCode.Normal, RoomCode.VIP, RoomCode.VVIP]

        lbldesc = QLabelRC("\nNote : Tiap tipe ruangan memiliki harga yang berbeda\n", "black")
        lbldesc.setFont(self.font)

        self.txtnama = EditLineRC("Test")

        # >>> SECOND LAYOUT <<<
        framelayout2 = QFrameRC("white")
        framelayout2.setContentsMargins(10, 10, 10, 10)
        layout2 = QGridLayout(framelayout2)

        # >>> ADD DATA <<<
        self.btnTambah = QPushButtonRC2("Pesan sekarang!", "Assets/img/button.png")
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
        self.layoutUtama.addWidget(framelayout2, 4, 0, 1, 9, Qt.AlignVCenter)
        self.layoutUtama.addWidget(self.btnTambah, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignRight)
        self.layoutUtama.addWidget(self.btnMainMenu, 5, 0, 1, 9, Qt.AlignBottom | Qt.AlignLeft)

        layout1.addWidget(lbljudul, 0, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(lblnomorRuangan, 1, 0, 1, 3, Qt.AlignLeft)
        layout1.addWidget(self.cmbnomorRuangan, 2, 0, 2, 3)
        layout1.addWidget(lbltipeRuangan, 1, 5, 1, 3)
        layout1.addWidget(self.cmbtipeRuangan, 2, 5, 2, 3)

        layout2.addWidget(lbldesc, 0, 0, 0, 0)

        self.setLayout(self.layoutUtama)
        self.show()

    @pyqtSlot()
    def insertData(self):
        self.id = "e"
        self.room_number = self.piltipeRuangan[self.cmbtipeRuangan.currentIndex()]
        self.room_code = self.pilnomorRuangan[self.cmbnomorRuangan.currentIndex()]
        self.status = "e"
        room = RoomOrm(self.id, self.room_number, self.room_code, self.status)
        try:
            RoomOrm.insertRoom(room)
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
        self.cmbtipeRuangan.setCurrentIndex(0)
        self.cmbnomorRuangan.setCurrentIndex(0)

#app = QApplication(sys.argv)
#emp = EmployeeView()
#emp.show()
#sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    BookView = BookView()
    sys.exit(app.exec_())