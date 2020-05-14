# from PyQt5.QtWidgets import *
# import sys
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from db.Orm.UserOrm import UserOrm
from GUI.ReusableComponent.EditLineRC import EditLineRC
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QPushButtonRC import QPushButtonRC
from GUI.MainMenu import MainMenu


class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1136, 833)
        self.setWindowTitle("LOGIN HOTEL")

        # =========== LAYOUT 1 SECTION ===========
        lbllogo = QLabelRC("yo", "yo")
        lbllogo.setPixmap(QtGui.QPixmap("Assets/img/sleep.jpg"))
        lbllogo.setAlignment(QtCore.Qt.AlignCenter)

        lblPresentBy = QLabelRC("Sleep tight", "black")
        lblPresentBy.setAlignment(QtCore.Qt.AlignCenter)
        lblCredit = QLabelRC("'Chilling out on the bed in your hotel room watching television, while wearing your own pajamas, is sometimes the best part of a vacation.'", "grey")
        lblCredit.setAlignment(QtCore.Qt.AlignCenter)

        # =========== LAYOUT 2 SECTION ===========
        lbljudul = QLabelRC("HOTEL", "black")
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(70)
        lbljudul.setFont(font)
        lbljudul.setAlignment(QtCore.Qt.AlignCenter)

        lblusername = QLabelRC("Username", "grey")
        lblpassword = QLabelRC("Password", "grey")
        # EditLine
        self.txtUsername = EditLineRC("")
        self.txtpassword = EditLineRC("")
        self.txtpassword.setEchoMode(QLineEdit.Password)
        # QPushButton
        self.btnLogin = QPushButtonRC("Login")
        self.btnLogin.clicked.connect(lambda: self.buttonClick())

        # =========== LAYOUT SECTION =============
        layout1 = QVBoxLayout()
        layout1.addWidget(lbllogo)
        layout1.addWidget(lblPresentBy)
        layout1.addWidget(lblCredit)

        layout2 = QVBoxLayout()
        layout2.setContentsMargins(45, 45, 45, 45)
        layout2.setSpacing(0)
        layout2.addWidget(lbljudul)
        layout2.addWidget(lblusername)
        layout2.addWidget(self.txtUsername)
        layout2.addWidget(lblpassword)
        layout2.addWidget(self.txtpassword)
        layout2.addWidget(self.btnLogin)

        layoutUtama = QHBoxLayout()
        layoutUtama.addLayout(layout1)
        layoutUtama.addLayout(layout2)

        self.setLayout(layoutUtama)
        self.show()

    @pyqtSlot()
    def buttonClick(self):
        username = self.txtUsername.text()
        password = self.txtpassword.text()
        checkLogin = UserOrm.verifyUser(username, password)
        if (checkLogin == True):
            self.switchMainMenu()
        else:
            msg = QMessageBox()
            msg.resize(250, 250)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username/Password tidak cocok!")
            msg.setWindowTitle("GAGAL")
            msg.exec_()

    @pyqtSlot()
    def switchMainMenu(self):
        username = self.txtUsername.text()
        authority = UserOrm.findOtoritas(username)
        self.mainMenu = MainMenu(username.upper(), authority)
        self.mainMenu.show()
        self.hide()

    def clear(self):
        self.txtUsername.setText("")
        self.txtpassword.setText("")
        self.txtUsername.setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginView = LoginView()
    sys.exit(app.exec_())