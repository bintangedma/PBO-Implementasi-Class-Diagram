from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QPushButton


class QPushButtonRC2(QPushButton):

    def __init__(self, text, iconPath):
        super().__init__()
        self.setStyleSheet("background-color :  rgb(0, 85, 255);\n"
                           "border : none;\n"
                           "border-radius : 10px;\n"
                           "height : 50%;\n"
                           "color : white;\n")
        self.setText(text)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(45, 45))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)