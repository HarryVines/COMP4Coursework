from PyQt4.QtGui import *
from PyQt4.QtCore import *

from comment_window import *
from comments_button import *

import sys

class InformationWindow(QMainWindow):
            def __init__(self):
                super().__init__()
			
                self.setWindowTitle("Suppliers Database")

                self.layout = QGridLayout()

                self.company_name = QLabel("Company Name:")
                self.owner_name = QLabel("Owner's Name:")
                self.company_address = QLabel("Address:")
                self.telephone_number = QLabel("Telephone Number:")
                self.email_address = QLabel("Email Address:")
                self.website = QLabel("Website:")
                self.parts_provided = QLabel("Parts Provided")
                self.part_prices = QLabel("Part Prices:")
                self.comment = CommentsWidget()
                self.back = QPushButton("Back")
                self.table = QTableWidget()
                self.table.setRowCount(10)
                self.table.setColumnCount(2)

                

                self.layout.addWidget(self.table)
                self.layout.addWidget(self.comment)
                self.layout.addWidget(self.back)
                
                self.widget = QWidget()
                self.widget.setLayout(self.layout)

                self.setCentralWidget(self.widget)

                self.comment.submit.clicked.connect(self.viewcomments)

            def viewcomments(self):
                self.vcomment = CommentWindow()
                self.vcomment.show()
                self.vcomment.raise_()
                self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InformationWindow()
    window.show()
    window.raise_()
    app.exec()
