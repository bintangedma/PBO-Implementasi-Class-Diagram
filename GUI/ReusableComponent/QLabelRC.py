from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class QLabelRC(QLabel):
    def __init__(self, text, colorName):
        super().__init__()
        self.setText(text)
        self.setWordWrap(True)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(75)

        self.setFont(font)
        self.setStyleSheet("color : "+colorName+";")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)