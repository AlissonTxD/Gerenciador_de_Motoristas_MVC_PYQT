from src.views.gui_view import gui_clash
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clashwindow = gui_clash()
    app.exec_()