from PyQt4.QtGui import *
from PyQt4.QtCore import *

from name_widget import *

class BackWidget(QWidget):
    BackEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.name = NameWidget()

        self.label = QLabel()
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.back.clicked.connect(self.display_back)

    def display_back(self):
        self.BackEntered.emit()

