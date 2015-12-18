from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from add_comment_window import *

class CommentWindow(QMainWindow):
            def __init__(self):
                super().__init__()

                self.setWindowTitle("Suppliers Database")
                
                self.title = QLabel("Comments:")
                self.comments = QWidgetView()
                self.submit = QPushButton("Add Comment")
                self.submit2 = QPushButton("Edit Comment")
                self.back = QPushButton("Back")

                self.layout = QVBoxLayout()

                self.layout.addWidget(self.title)
                self.layout.addWidget(self.comments)
                self.layout.addWidget(self.submit)
                self.layout.addWidget(self.submit2)
                self.layout.addWidget(self.back)

                row = -1
                for supplier in data:
                    column= 0
                    row = row +1
                for field in supplier:
                    self.table.setItem(row,column, QTableWidgetItem(str(field)))
                    column = column +1 
                row = -1

                self.widget = QWidget()
                self.widget.setLayout(self.layout)

                self.setCentralWidget(self.widget)

                self.submit.clicked.connect(self.addcomment)

            def addcomment(self):
               self.addcomment = AddCommentWindow()
               self.addcomment.show()
               self.addcomment.raise_()
               self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommentWindow()
    window.show()
    window.raise_()
    app.exec()
