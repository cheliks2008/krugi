import sys
import random

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtGui
from UI import Ui_MainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class LSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.yl)

    def yl(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            self.qpaint = QtGui.QPainter()
            self.qpaint.begin(self)
            self.qpaint.setBrush(QtGui.QColor(random.randint(0, 255), random.randint(0, 255),
                                              random.randint(0, 255)))
            for i in range(random.randint(1, 10)):
                o = random.randint(3, self.height())
                self.qpaint.drawRoundedRect(random.randint(0, self.height()), random.randint(0, self.width()), o,
                                            o, o / 2, o / 2)
            self.qpaint.end()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LSystem()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())