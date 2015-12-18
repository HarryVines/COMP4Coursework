from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from comment_window import *

from search_widget_resultspage import *
from searchbar_widget import *
from back_widget import *
from add_info_window import *

from Database import *

class ResultsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suppliers Database")

        self.layout = QVBoxLayout()

        self.searchbar = SearchBarWidget()
        self.search = SearchWidget1()
        self.result = QLabel("Search Results:")
        self.back = BackWidget()

        data = g_database.GetAllSuppliers()
            
        self.table = QTableWidget()

        counter = 0
        for supplier in data:
            counter = counter +1


        self.table.setRowCount(counter)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["Company Name"])

##        row = -1
##        for supplier in data:
##            column= 0
##            row = row +1
##            for field in supplier:
##                self.table.setItem(row,column, QTableWidgetItem(str(field)))
##                column = column +1 
        row = -1

        for supplier in data:
            row = row+1
            self.table.setItem(row,0, QTableWidgetItem(str(supplier[1])))
            


        
        
        self.addinfo = AddSupplierWindow()

        self.layout.addWidget(self.searchbar)
        self.layout.addWidget(self.search)
        self.layout.addWidget(self.result)
        self.layout.addWidget(self.table)
        self.layout.addWidget(self.back)

        


        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)

        self.back.add.clicked.connect(self.add_supplier)

    def add_supplier(self):
        self.addsupplier = AddSupplierWindow()
        self.addsupplier.show()
        self.addsupplier.raise_()
        self.hide()
        



        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResultsWindow()
    window.show()
    window.raise_()
    app.exec()
          

         


         
