from PyQt4.QtGui import *
from PyQt4.QtCore import *


class DescriptionWidget(QWidget):
		SearchEntered = pyqtSignal()
		def __init__(self):
			super().__init__()
			
			self.label = QLabel("Description to come here soon...")
			
			self.layout = QVBoxLayout()
			
			self.layout.addWidget(self.label)
			
			self.setLayout(self.layout)