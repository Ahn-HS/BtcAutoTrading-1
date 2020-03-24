import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic
import qdarkstyle

form_class = uic.loadUiType("design_main.ui")[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        # init ui styles
        self.setupUi(self)
        self._apply_style()

    def _apply_style(self):
        # setup stylesheet
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # font
        default_font = QtGui.QFont('lib/fonts/NotoSansCJKkr-Regular.otf')
        self.setFont(default_font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
