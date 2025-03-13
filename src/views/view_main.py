from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon

from src.utils import resource_path

UI_PATH = resource_path("src/views/main_gui_mvc_motoristas.ui")  # Path do ui


class ViewMain(QMainWindow):
    def __init__(self,controller) -> None:
        super(ViewMain, self).__init__()
        uic.loadUi(UI_PATH, self)
        self.setWindowIcon(QIcon(resource_path("src/midia/logo/icone.ico")))
        self.controller = controller

        #aba nome
        self.btn_name_search = self.findChild(QPushButton, "btn_name_search")
        self.lineedit_name_search = self.findChild(QLineEdit, "lineedit_name_search")
        self.textedit_name_search = self.findChild(QTextEdit, "textedit_name_search")
        #aba placa
        self.btn_plate_search = self.findChild(QPushButton, "btn_plate_search")
        self.lineedit_plate_search = self.findChild(QLineEdit, "lineedit_plate_search")
        self.textedit_plate_search = self.findChild(QTextEdit, "textedit_plate_search")

        #aba registro

        #aba delete

        self.btn_name_search.clicked.connect(lambda: self.controller.search_by_name(self.lineedit_name_search.text()))