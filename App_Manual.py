


from PyQt5.QtWidgets import *


if __name__ == "__main__":
	app = QApplication([])
	window = QWidget()
	layout = QFormLayout()
	form = Form()
	form.setupUi(window)
	window.show()
	app.exec_()