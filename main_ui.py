import sys
#import main
from controller import Controller
from PyQt6 import QtWidgets
from spotify_ui_v3 import Ui_MainWindow
#from main import playlist, user_stats
#from user_stats import User
from view import MainWindow
from model import Model


def main():
    app = QtWidgets.QApplication([])
    
    view = MainWindow()
    view.show()

    model = Model()

    controller = Controller(view, model)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()



"""
# Esta clase en realidad pertenece al view

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #Intento cambiar le nombre de un label de la aplicacion con .setText
        #self.login_exitoso.setText("makanaki gaaaa")

#user_stats.get_user_data()

"""
