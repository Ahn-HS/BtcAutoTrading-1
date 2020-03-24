import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import qdarkstyle

# load qt designer ui file
FormClass, QtBaseClass = uic.loadUiType("design_main.ui")


# main window class
class MainWindow(QMainWindow, FormClass):
    def __init__(self):
        super().__init__()

        # init ui styles
        self.setupUi(self)
        self._apply_style()

    def _apply_style(self):
        # setup stylesheet
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
