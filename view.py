from PyQt6 import QtCore, QtGui, QtWidgets
from spotify_ui_v4 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #Se configura la GUI usando Qt designer
        self.setupUi(self)

    # Método que muestra el cover en la GUI
    def cover_img(self, image):
        cover_img = QtGui.QPixmap(image)
        self.cover_qlabel.setPixmap(cover_img)