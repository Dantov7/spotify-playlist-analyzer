import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

from spotify_ui_v1 import Ui_MainWindow

# Creamos primera clase con un solo widget presionable para el login
class Window(QMainWindow):
    """Main window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        # Use a QPushButton for the central widget
        self.__centralWidget = QPushButton("Inicia sesión en Spotify para empezar")

        # Connect the .clicked() signal with the .LoginBtnClicked() slot
        self.__centralWidget.clicked.connect(self.LoginBtnClicked)

        # Acá define como widget central de la instancia QmainWindow el self.__centralWidget
        self.setCentralWidget(self.__centralWidget)


    # Create a slot for launching the employee dialog
    def LoginBtnClicked(self):
        """Launch the employee dialog.""" # Instacia la clase y arranca la aplicacion con el exec
        playlist_analyzer_gui = Playlist_Analyzer_GUI(self)
        #playlist_analyzer_gui.exec()
    


# Creamos la clase de la interfaz graáfica del analizador
class Playlist_Analyzer_GUI(QMainWindow):
    """playlist UI dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Creamos una instanciade la gui llamando la clase Ui_MainWindow del spotify_ui_py
        self.__ui = Ui_MainWindow()
        # Run the .setupUi() method to show the GUI spotify_ui_py
        self.__ui.setupUi(self)
        self.exec()


# Main Loop de la aplicación: 

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the application's main window
    win = Window()
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())


