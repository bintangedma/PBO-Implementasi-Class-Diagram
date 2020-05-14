from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class EditLineRC(QLineEdit):

    def __init__(self, placeholder):
        super().__init__()
        self.setStyleSheet("border : 0;\n"
                           "outline : 0;\n"
                           "background : white;\n"
                           "border-top : 2px solid rgb(125, 15, 15);\n"
                           "border-bottom : 2px solid rgb(125, 15, 15);")
        self.setPlaceholderText(placeholder)
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setWeight(55)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
