from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox


class QComboBoxRC(QComboBox):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("border : 0;\n"
                           "outline : 0;\n"
                           "background : white;\n"
                           "border-bottom : 2px solid rgb(125, 15, 15);\n"
                           "border-top : 2px solid rgb(125, 15, 15);")
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(55)

        self.setFont(font)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
