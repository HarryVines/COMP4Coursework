from PyQt4.QtGui import *
from PyQt4.QtCore import *

from comment_window import *

class CommentsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.submit = QPushButton("View Comments")
        self.submit2 = QPushButton("Edit Information")        

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.submit)
        self.layout.addWidget(self.submit2)

        self.setLayout(self.layout)


        
