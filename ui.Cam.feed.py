from PyQt5 import uic, QtWidgets
from Thread import Thread

import sys

class UI(QtWidgets.QMainWindow):
	def screen(self):
  #loading Ui file named untitled.ui. It contains a label box named screen
		uic.loadUi('untitled.ui', self)
		self.myThread = Thread(self)
		self.myThread.stream = 0
		self.myThread.changePixmap.connect(self.screen.setPixmap)
		self.myThread.start()

		
app = QtWidgets.QApplication(sys.argv)
myObject = UI()
myObject.screen()
myObject.show()
sys.exit(app.exec_())
