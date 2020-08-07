from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myWindow(QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(200, 200, 300, 300) # xpos, ypos, width, height
        self.setWindowTitle('Scissors Paper Rock')
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My Label")
        self.label.move(50, 50)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)  

    def clicked(self):
        self.label.setText("You presed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    """ SPR Window Specifications """
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())

window()