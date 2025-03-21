import sys

from PyQt5.QtWidgets import QApplication

from src.controllers import ControllerMain
from src.views import ViewMain


def start() -> None:
    app = QApplication(sys.argv)
    controller = ControllerMain()
    view = ViewMain(controller)
    view.show()
    app.exec_()
