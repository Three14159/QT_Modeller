from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from MainWindow import Ui_MainWindow
from PyQt5 import uic
import sys

# From Designer, save ui to MainWindow.ui.  File name is arbitrary.
# Program can be run from Call Designed.  Or......
# Convert ui to Python Class via command line:
# pyuic5 MainWindow.ui -o MainWindow.py
# Code below instantiates this class.

# Do not make any changes to converted file MainWindow.py, they will all be lost.

class TMainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(TMainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

def CallDesigned(uiFile):
	# CallDesigned("MainWindow.ui")
	Form, Window = uic.loadUiType(uiFile)
	app = QApplication([])
	window = Window()
	form = Form()
	form.setupUi(window)
	window.show()
	app.exec_()

def RunApp():
	app = QApplication([])
	application = TMainWindow()
	application.show()
	sys.exit(app.exec_())



if __name__ == "__main__":
	RunApp()
