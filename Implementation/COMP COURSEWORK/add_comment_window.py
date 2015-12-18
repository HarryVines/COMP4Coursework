from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from Database import *

class AddCommentWindow(QMainWindow):
            def __init__(self):
                super().__init__()

                self.setWindowTitle("Suppliers Database")

                
                self.title1 = QLabel("Please Rate your experience with the supplier:")
                self.title = QLabel("Please enter a comment: ")
                self.comment = QLineEdit()
                self.add = QPushButton("Add")
                self.back = QPushButton("Back")
                self.rating = QSpinBox()

                self.add.clicked.connect(self.onClickAddComment)
                
                self.rating.setValue(5)
                self.rating.setMaximum(10)

                self.layout = QVBoxLayout()
                
                self.layout.addWidget(self.title1)
                self.layout.addWidget(self.rating)
                self.layout.addWidget(self.title)
                self.layout.addWidget(self.comment)
                self.layout.addWidget(self.add)
                self.layout.addWidget(self.back)


                self.widget = QWidget()
                self.widget.setLayout(self.layout)

                self.setCentralWidget(self.widget)

            def onClickAddComment(self):
                g_database.add_comment(self.comment.text(),self.rating.text())


                

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddCommentWindow()
    window.show()
    window.raise_()
    app.exec()
