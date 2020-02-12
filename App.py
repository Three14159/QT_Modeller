from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


if __name__ == "__main__":
	Form, Window = uic.loadUiType("MainWindow.ui")
	app = QApplication([])
	window = Window()
	form = Form()
	form.setupUi(window)
	window.show()
	app.exec_()