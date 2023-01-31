import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Spotify Playlist Analyzer')
window.setGeometry(0,0,300,300)
window.move(200,200)

hello_label = QLabel("Daniela aqui va tu codigo", parent=window)
hello_label.move(60,30) #posicion relativa a su padre window

window.show()

sys.exit(app.exec())


        
# ME QUEDE EN MINUTO 42 DEL VIDEO