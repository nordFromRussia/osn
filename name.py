import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image')
        self.setGeometry(50, 50, 640, 480)

        but = QPushButton(self)
        but.setIcon(QIcon('Без имени-1.png'))
        but.setIconSize(QSize(75, 75))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())