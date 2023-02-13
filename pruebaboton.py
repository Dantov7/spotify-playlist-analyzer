import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget



app = QApplication(sys.argv)
window = QMainWindow()

widget = QWidget()
layout = QVBoxLayout()

line_edit = QLineEdit()
layout.addWidget(line_edit)

button = QPushButton("Guardar texto")
button.clicked.connect(handle_button_click)
layout.addWidget(button)

widget.setLayout(layout)
window.setCentralWidget(widget)
window.show()

sys.exit(app.exec())

def handle_button_click():
    text = line_edit.text()
    # Hacer algo con el texto aquí
    print (text)
    print("este es el texto: " + text)