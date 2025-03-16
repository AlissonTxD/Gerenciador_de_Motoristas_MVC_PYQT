import sys

from PyQt5.QtWidgets import QApplication

from src.controllers import ControllerMain
from src.views import ViewMain


def start() -> None:
    app = QApplication(sys.argv)
    controller = ControllerMain(None)
    view = ViewMain(controller)
    controller.view = view
    view.show()
    app.exec_()
