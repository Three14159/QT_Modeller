import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

from MainWindow import Ui_MainWindow

import NRLSQLite as NRLSQ
import NRLDotComObjects as NRLOBJ

# From Designer, save ui to MainWindow.ui.  File name is arbitrary.
# Program can be run from Call Designed.  Or......
# Convert ui to Python Class via command line:
# pyuic5 MainWindow.ui -o MainWindow.py
# Code below instantiates this class.

# Do not make any changes to converted file MainWindow.py, they will all be lost.

def CollateLineupsBtn_OnClick():
	print("I hope she rots.  Lets see how she feels when I rub 'YOU cant have THIS' in her face.  Gonna be fun")

class TMainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(TMainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.CollateLineupsBtn.clicked.connect(self.CollateLineupsBtn_OnClick)


	def GetSQPath(self):
		_sq_path = str(self.ui.DBConnectionTextEdit.toPlainText())
		return _sq_path

	def CollateLineupsBtn_OnClick(self):
		print("QT message: Collation Starting")
		_sq_path = self.GetSQPath()
		print(f"QT message: SQPath = {_sq_path}")
		NRLOBJ.CollateLineups(_sq_path)
		print("QT message:  Lineups Collated")

def CallDesigned(uiFile):
	# usage:   CallDesigned("MainWindow.ui")
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
