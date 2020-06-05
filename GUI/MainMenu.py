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
from Class.Authority import Authority
from GUI.ReusableComponent.QPushButtonRC import QPushButtonRC

class MainMenu(QWidget):
    def __init__(self, username, authority):
        super().__init__()
        self.showMaximized()
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle("MAIN MENU")

        # >>>> MENU SECTION <<<<
        MenuBar = QFrameRC("white")
        MenuBar.setContentsMargins(10, 10, 10, 10)

        MenuLayout = QGridLayout(MenuBar)
        MenuLayout.setSpacing(5)
        self.btnCheckIn = QPushButtonRC2("Book now", "assets/img/bed.png")
        self.btnRoom = QPushButtonRC2("Occupied Room", "assets/img/no.png")
        self.btnBRUH2 = QPushButtonRC2("Reserved", "assets/img/back.png")


        # >>>> MENU EVENT SECTION <<<<
        self.btnCheckIn.clicked.connect(lambda: self.bookSlot())
        #self.btnBRUH2.clicked.connect(lambda: self.logOutSlot())
        self.btnRoom.clicked.connect(lambda: self.logOutSlot())
        #self.btnRoom.clicked.connect(lambda: self.roomSlot())

        # >>>> LOGOUT SECTION <<<<
        LogoutBar = QFrameRC("transparent")
        LogoutBar.setContentsMargins(10, 10, 10, 10)

        LogoutLayout = QGridLayout(LogoutBar)
        LogoutLayout.setSpacing(5)

        # >>>> BOTTOMBAR SECTION <<<<
        frameBottomBar = QFrameRC("white")
        frameBottomBar.setContentsMargins(10, 10, 10, 10)

        bottomBarLayout = QGridLayout(frameBottomBar)
        bottomBarLayout.setSpacing(5)
        btnMainMenu = QPushButtonRC2("Tambah Data : ", "")
        self.btnAdministrator = QPushButtonRC2("Administrator", "assets/img/add.png")
        self.btnEmployee = QPushButtonRC2("Employee", "assets/img/add.png")
        self.btnReceptionist = QPushButtonRC2("Receptionist", "assets/img/add.png")
        self.btnMarketing_crew = QPushButtonRC2("Marketing Crew", "assets/img/add.png")
        self.btnCashier = QPushButtonRC2("Cashier", "assets/img/add.png")
        self.btnVisitor = QPushButtonRC2("Visitor", "assets/img/add.png")
        self.btnUser = QPushButtonRC2("User", "assets/img/add.png")
        self.btnLogOut = QPushButtonRC2("Log Out", "assets/img/logout.png")

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
        welcome = QLabelRC("Selamat datang,", "white")
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
        bottomBarLayout.addWidget(self.btnLogOut, 0, 7)
        #Menu
        MenuLayout.addWidget(self.btnCheckIn, 0, 0)
        MenuLayout.addWidget(self.btnRoom, 0, 1)
        MenuLayout.addWidget(self.btnBRUH2, 0, 2)
        LogoutLayout.addWidget(self.btnLogOut, 0, 0, QtCore.Qt.AlignRight)
        #Header
        headerLayout.addWidget(self.authority, 0, 0, QtCore.Qt.AlignLeft)
        headerLayout.addWidget(profile, 0, 2, QtCore.Qt.AlignRight)

        frameLayout.addLayout(frameLayoutLeft)
        frameLayout.addLayout(frameLayoutRight)

        frameLayoutLeft.addWidget(welcome)
        frameLayoutLeft.addWidget(self.username)
        frameLayoutLeft.addWidget(quote)

        frameLayoutRight.addWidget(lbllogo)
        #Main
        layoutUtama = QGridLayout()
        layoutUtama.addWidget(frameTitle, 0, 1, 1, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameDashboard, 1, 1, 5, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(frameBottomBar, 6, 1, 10, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(MenuBar, 13, 1, 10, 9, QtCore.Qt.AlignTop)
        layoutUtama.addWidget(LogoutBar, 18, 1, 10, 9, QtCore.Qt.AlignBottom)
        layoutUtama.setSpacing(10)
        self.authorityVisible()
        self.setLayout(layoutUtama)

    @pyqtSlot()
    def roomSlot(self):
        from GUI.RoomGUI import RoomView
        self.room = RoomView()
        self.room.show()

    @pyqtSlot()
    def bookSlot(self):
        from GUI.BookGUI import BookView
        self.book = BookView()
        self.book.show()

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


    @pyqtSlot()
    def empSlot(self):
        from GUI.EmployeeGUI import EmployeeView
        self.EmployeeView = EmployeeView()
        self.EmployeeView.show()


    @pyqtSlot()
    def recSlot(self):
        from GUI.ReceptionistGUI import ReceptionistView
        self.ReceptionistView = ReceptionistView()
        self.ReceptionistView.show()

    @pyqtSlot()
    def mcSlot(self):
        from GUI.Marketing_crewGUI import Marketing_crewView
        self.mcView = Marketing_crewView()
        self.mcView.show()

    @pyqtSlot()
    def userSlot(self):
        from View.UserView import UserView
        self.userView = UserView()
        self.userView.show()

    @pyqtSlot()
    def casSlot(self):
        from GUI.CashierGUI import CashierView
        self.casView = CashierView()
        self.casView.show()

    @pyqtSlot()
    def visSlot(self):
        from GUI.VisitorGUI import VisitorView
        self.visView = VisitorView()
        self.visView.show()

    def authorityVisible(self):
        authority = self.authority.text()
        if (authority == str(Authority.Employee)):
            self.btnAdministrator.setVisible(False)
            self.btnReceptionist.setVisible(False)
            self.btnMarketing_crew.setVisible(False)
            self.btnCashier.setVisible(False)
            self.btnVisitor.setVisible(False)
        elif (authority == str(Authority.Receptionist)):
            self.btnAdministrator.setVisible(False)
            self.btnEmployee.setVisible(False)
            self.btnMarketing_crew.setVisible(False)
            self.btnCashier.setVisible(False)
            self.btnVisitor.setVisible(False)
        elif (authority == str(Authority.Marketing_crew)):
            self.btnAdministrator.setVisible(False)
            self.btnEmployee.setVisible(False)
            self.btnReceptionist.setVisible(False)
            self.btnCashier.setVisible(False)
            self.btnVisitor.setVisible(False)
        elif (authority == str(Authority.Cashier)):
            self.btnAdministrator.setVisible(False)
            self.btnEmployee.setVisible(False)
            self.btnReceptionist.setVisible(False)
            self.btnMarketing_crew.setVisible(False)
            self.btnVisitor.setVisible(False)
        elif (authority == str(Authority.Visitor)):
            self.btnAdministrator.setVisible(False)
            self.btnEmployee.setVisible(False)
            self.btnReceptionist.setVisible(False)
            self.btnCashier.setVisible(False)
            self.btnMarketing_crew.setVisible(False)
        else:
            self.btnVisitor.setVisible(False)