from PyQt4.QtGui import *
from PyQt4.QtCore import *

from search_widget_coursework import *
from searchbar_widget import *
from top_widget import *
from description_widget import *
from exit_widget import *
from results_window import *

import sys

class MainWindow(QMainWindow):
        def __init__(self):
                super().__init__()
			
                self.setWindowTitle("Suppliers Database")

                self.layout = QGridLayout()

                self.search = SearchWidget()
                self.top = TopWidget()
                self.searchbar = SearchBarWidget()
                self.description = DescriptionWidget()
                self.exit = ExitWidget()
                self.result = ResultsWindow()

                self.layout.addWidget(self.top)
                self.layout.addWidget(self.searchbar)
                self.layout.addWidget(self.search)
                self.layout.addWidget(self.description)
                self.layout.addWidget(self.exit)

                self.widget = QWidget()
                self.widget.setLayout(self.layout)

                self.setCentralWidget(self.widget)
                self.search.submit.clicked.connect(self.ResultsPage)
                self.result.back.back.clicked.connect(self.GoBack)

        def GoBack(self):
                self.show()
                self.raise_()
                self.result.hide()
        
        def ResultsPage(self):
                self.hide()

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec()
    

