from PyQt6 import QtCore, QtGui, QtWidgets
from spotify_ui_v4 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def cover_img(self,image):
        cover_img = QtGui.QPixmap(image)
        self.cover_qlabel.setPixmap(cover_img)