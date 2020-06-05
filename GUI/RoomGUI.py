import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from db.Orm.RoomOrm import RoomOrm
from db.Orm.UserOrm import UserOrm
from GUI.ReusableComponent.QLabelRC import QLabelRC
from GUI.ReusableComponent.QTableWidgetRC import QTableWidgetRC


class RoomView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROOM VIEW")
        self.resize(550, 350)

        data = RoomOrm.showRoom()
        roomNumber, roomCode, status = [], [], []

        for i in data:
            roomNumber = roomNumber + [i[0]]
            roomCode = roomCode + [i[1]]
            status = status + [i[2]]

        result = {'ROOM NUMBER': roomNumber, 'ROOM TYPE': roomCode, 'STATUS': status}

        self.tableWidgetRoom = QTableWidgetRC(result, len(data), 3)

        layoutUtama = QVBoxLayout(self)
        layoutUtama.addWidget(self.tableWidgetRoom)
        self.setLayout(layoutUtama)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    RookView = RoomView()
    sys.exit(app.exec_())