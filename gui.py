import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget

from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QPushButton



app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Spotify Playlist Analyzer')
window.setGeometry(0,0,300,300)
window.move(200,200)

hello_label = QLabel("Daniela aqui va tu codigo", parent=window)
hello_label.move(60,30) #posicion relativa a su padre window


layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
layout.addWidget(QPushButton('teste'))

window.setLayout(layout)




window.show()

sys.exit(app.exec())


        
# ME QUEDE EN MINUTO 42 DEL VIDEO