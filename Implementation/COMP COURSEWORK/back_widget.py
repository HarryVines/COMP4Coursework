from PyQt4.QtGui import *
from PyQt4.QtCore import *

from searchbar_widget import *

class BackWidget(QWidget):
		SearchEntered = pyqtSignal()
		def __init__(self):
			super().__init__()

			self.back = QPushButton("Back")
			self.add = QPushButton("Add Supplier")

			self.layout = QGridLayout()
		

			self.layout.addWidget(self.back,2,0)
			self.layout.addWidget(self.add,2,1)

			self.setLayout(self.layout)


