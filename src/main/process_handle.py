from src.views.view_main import ViewMain
from src.controllers.controller_main import ControllerMain
from PyQt5.QtWidgets import QApplication
import sys

def start() -> None:
    app = QApplication(sys.argv)
    controller = ControllerMain(None)
    view = ViewMain(controller)
    controller.view = view
    view.show()
    app.exec_()