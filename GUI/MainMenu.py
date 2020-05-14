import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from db.Orm.UserOrm import UserOrm
from GUI.ReusableComponent.EditLineRC import EditLineRC
from GUI.ReusableComponent.QComboBoxRC import QComboBoxRC
from GUI.ReusableComponent.QFrameRC import QFrameRC
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QPushButtonRC2 import QPushButtonRC2



class MainMenu(QWidget):
    def __init__(self, username, authority):
        super().__init__()
        self.showMaximized()
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle("MAIN MENU")

        # >>>> BOTTOMBAR SECTION <<<<
        frameBottomBar = QFrameRC("white")
        frameBottomBar.setContentsMargins(10, 10, 10, 10)

        bottomBarLayout = QGridLayout(frameBottomBar)
        bottomBarLayout.setSpacing(5)
        btnMainMenu = QPushButtonRC2("Main Menu", "Assets/img/button.png")
        self.btnAdministrator = QPushButtonRC2("Form Admin", "")
        self.btnEmployee = QPushButtonRC2("Form Employee", "")
        self.btnReceptionist = QPushButtonRC2("Form Receptionist", "")
        self.btnMarketing_crew = QPushButtonRC2("Form Marketing Crew", "")
        self.btnCashier = QPushButtonRC2("Form Cashier", "")
        self.btnVisitor = QPushButtonRC2("Form Visitor", "")
        self.btnUser = QPushButtonRC2("Form User", "")
        self.btnLogOut = QPushButtonRC2("Log Out", "")

        # >>>> EVENT SECTION <<<<
        self.btnLogOut.clicked.connect(lambda: self.logOutSlot())
        self.btnAdministrator.clicked.connect(lambda: self.adminSlot())
        self.btnEmployee.clicked.connect(lambda: self.empSlot())
        self.btnReceptionist.clicked.connect(lambda: self.recSlot())
        self.btnMarketing_crew.clicked.connect(lambda: self.mcSlot())
        self.btnCashier.clicked.connect(lambda: self.casSlot())
        self.btnVisitor.clicked.connect(lambda: self.visSlot())
        self.btnUser.clicked.connect(lambda: self.userSlot())

        # >>>> DASHBOARD SECTION TITLE <<<<
        frameTitle = QFrameRC("white")

        headerLayout = QGridLayout(frameTitle)
        self.authority = QLabelRC(str(authority), "black")
        self.authority.setAlignment(QtCore.Qt.AlignLeft)
        profile = QPushButtonRC2("", "assets/img/profile.png")

        # >>>> DASHBOARD SECTION BODY <<<<
        frameDashboard = QFrameRC("rgb(125, 15, 15)")
        frameLayout = QHBoxLayout(frameDashboard)
        frameLayout.setContentsMargins(40, 40, 40, 40)

        frameLayoutLeft = QVBoxLayout()
        frameLayoutRight = QVBoxLayout()

        font = QtGui.QFont()
        font.setFamily("Arial Rounded")
        font.setPointSize(11)
        font.setWeight(50)
        welcome = QLabelRC("Welcome", "white")
        welcome.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(12)
        font.setWeight(75)
        self.username = QLabelRC(username, "white")
        self.username.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Arial Rounded")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(50)
        quote = QLabelRC("\n\n\n\n\nWhen you get into a hotel room, you lock the door, and you know there is a secrecy, there is a luxury, there is fantasy. There is comfort. There is reassurance.", "white")
        quote.setFont(font)

        lbllogo = QLabelRC("", "")
        lbllogo.setPixmap(QtGui.QPixmap("assets/img/medical256.png"))
        lbllogo.setAlignment(QtCore.Qt.AlignRight)

        # >>>> LAYOUT SECTION <<<<
        bottomBarLayout.addWidget(btnMainMenu, 0, 0)
        bottomBarLayout.addWidget(self.btnAdministrator, 0, 1)
        bottomBarLayout.addWidget(self.btnEmployee, 0, 2)
        bottomBarLayout.addWidget(self.btnReceptionist, 0, 3)
        bottomBarLayout.addWidget(self.btnMarketing_crew, 0, 4)
        bottomBarLayout.addWidget(self.btnCashier, 0, 5)
        bottomBarLayout.addWidget(self.btnVisitor, 0, 6)
        bottomBarLayout.addWidget(self.btnLogOut, 0, 7, QtCore.Qt.AlignBottom)

        headerLayout.addWidget(self.authority, 0, 0, QtCore.Qt.AlignLeft)
        headerLayout.addWidget(profile, 0, 2, QtCore.Qt.AlignRight)

        frameLayout.addLayout(frameLayoutLeft)
        frameLayout.addLayout(frameLayoutRight)

        frameLayoutLeft.addWidget(welcome)
        frameLayoutLeft.addWidget(self.username)
        frameLayoutLeft.addWidget(quote)

        frameLayoutRight.addWidget(lbllogo)

        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameTitle, 0, 1, 1, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameDashboard, 1, 1, 5, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameBottomBar, 6, 1, 10, 9, QtCore.Qt.AlignTop)
        layoutUtama.setSpacing(10)
        self.setLayout(layoutUtama)

    @pyqtSlot()
    def logOutSlot(self):
        from GUI.AuthenticationGUI import LoginView
        self.login = LoginView()
        self.login.show()
        self.close()

    @pyqtSlot()
    def adminSlot(self):
        from GUI.administratorGUI import AdminView
        self.AdminView = AdminView()
        self.AdminView.show()
        self.close()

    @pyqtSlot()
    def empSlot(self):
        from GUI.EmployeeGUI import EmployeeView
        self.employeeView = EmployeeView()
        self.employeeView.show()
        self.close()

    @pyqtSlot()
    def recSlot(self):
        from GUI.receptionistGUI import ReceptionistView
        self.receptionistView = ReceptionistView()
        self.receptionistView.show()
        self.close()

    @pyqtSlot()
    def mcSlot(self):
        from GUI.marketingcrewGUI import Marketing_crewView
        self.mcView = Marketing_crewView()
        self.mcView.show()
        self.close()

    @pyqtSlot()
    def userSlot(self):
        from View.UserView import UserView
        self.userView = UserView()
        self.userView.show()
        self.close()

    @pyqtSlot()
    def casSlot(self):
        from GUI.cashierGUI import CashierView
        self.casView = CashierView()
        self.casView.show()
        self.close()

    @pyqtSlot()
    def visSlot(self):
        from GUI.visitorGUI import VisitorView
        self.visView = VisitorView()
        self.visView.show()
        self.close()
