from PyQt6 import QtWidgets, QtGui

app = QtWidgets.QApplication([])

label = QtWidgets.QLabel()
label.setScaledContents(True)
label.setFixedSize(350, 350)

pixmap = QtGui.QPixmap("cover.jpg")
label.setPixmap(pixmap)

label.show()

app.exec()