from src.views.gui_view import gui_clash
from PyQt5.QtWidgets import QApplication
import sys

def start() -> None:
    app = QApplication(sys.argv)
    interface = gui_clash()
    app.exec_()