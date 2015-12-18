from PyQt4.QtGui import *
from PyQt4.QtCore import *


class SearchBarWidget(QWidget):
    SearchEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.searchbar = QLineEdit()

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.searchbar)

        self.setLayout(self.layout)
