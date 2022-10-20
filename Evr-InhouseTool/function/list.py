import os
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_List(object):
    def setupList(self, MainView):
        print("asset Import")
        self.listView = QtWidgets.QListWidget(MainView)