from PyQt6 import QtCore, QtGui, QtWidgets
from spotify_ui_v3 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Intento cambiar le nombre de un label de la aplicacion con .setText
        #self.login_exitoso.setText("makanaki gaaaa")
    
    def cover_img(self,image):
        cover_img = QtGui.QPixmap(image)
        self.cover_qlabel.setPixmap(cover_img)


