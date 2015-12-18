from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from Database import *

class AddSupplierWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suppliers Database")

        self.title = QLabel("Please add the relevent information:")

        self.info1 = QLabel("Company Name:")
        self.info2 = QLabel("Owner's Name:")
        self.info3 = QLabel("Address:")
        self.info4 = QLabel("Telephone Number:")
        self.info5 = QLabel("Email Address")
        self.info6 = QLabel("Website:")
        self.info7 = QLabel("Parts Provided:")
        self.info8 = QLabel("Part Prices:")
        self.edit = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()
        self.edit7 = QLineEdit()
        self.edit8 = QLineEdit()

        self.btnAddSupplier = QPushButton("Add Supplier")
        self.btnBack = QPushButton("Back")

        self.btnAddSupplier.clicked.connect(self.onClickAddSupplier)

        self.layout = QGridLayout()

        self.layout.addWidget(self.title,0,1)
        self.layout.addWidget(self.info1,1,1)
        self.layout.addWidget(self.info2,2,1)
        self.layout.addWidget(self.info3,3,1)
        self.layout.addWidget(self.info4,4,1)
        self.layout.addWidget(self.info5,5,1)
        self.layout.addWidget(self.info6,6,1)
        self.layout.addWidget(self.info7,7,1)
        self.layout.addWidget(self.info8,8,1)
        self.layout.addWidget(self.edit,1,2)
        self.layout.addWidget(self.edit2,2,2)
        self.layout.addWidget(self.edit3,3,2)
        self.layout.addWidget(self.edit4,4,2)
        self.layout.addWidget(self.edit5,5,2)
        self.layout.addWidget(self.edit6,6,2)
        self.layout.addWidget(self.edit7,7,2)
        self.layout.addWidget(self.edit8,8,2)
        self.layout.addWidget(self.btnAddSupplier,9,2)
        self.layout.addWidget(self.btnBack,9,3)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

    def onClickAddSupplier(self):
        g_database.add_supplier(self.edit.text(),self.edit2.text(),self.edit3.text(),self.edit4.text(),self.edit5.text(),self.edit6.text())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddSupplierWindow()
    window.show()
    window.raise_()
    app.exec()
