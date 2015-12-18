from PyQt4.QtGui import *
from PyQt4.QtCore import *


class ExitWidget(QWidget):
		SearchEntered = pyqtSignal()
		def __init__(self):
			super().__init__()
			
			self.button = QPushButton("Exit")
			
			self.layout = QGridLayout()
			
			self.layout.addWidget(self.button,7,3)
			
			self.setLayout(self.layout)