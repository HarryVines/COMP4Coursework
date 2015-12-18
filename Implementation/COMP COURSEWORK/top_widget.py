from PyQt4.QtGui import *
from PyQt4.QtCore import *


class TopWidget(QWidget):
		SearchEntered = pyqtSignal()
		def __init__(self):
			super().__init__()
			
			self.label = QLabel("Please enter a part or supplier's name: ")
			
			self.layout = QGridLayout()
			
			self.layout.addWidget(self.label,0,0)
			
			self.setLayout(self.layout)