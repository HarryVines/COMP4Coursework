from PyQt4.QtGui import *
from PyQt4.QtCore import *

from searchbar_widget import *

from results_window import *

class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.submit = QPushButton("Search")
        self.label2 = QLabel("Filters: ")
        self.dropdown = QComboBox()
        self.dropdown.addItem("None")
        self.dropdown.addItem("Part Name")
        self.dropdown.addItem("Supplier Name")	

        self.layout = QGridLayout()


        self.layout.addWidget(self.submit,2,0)
        self.layout.addWidget(self.label2,2,1)
        self.layout.addWidget(self.dropdown,2,2)

        self.setLayout(self.layout)

        self.submit.clicked.connect(self.searched)

    def searched(self):
        self.searched = ResultsWindow()
        self.searched.show()
        self.searched.raise_()
        self.hide()




