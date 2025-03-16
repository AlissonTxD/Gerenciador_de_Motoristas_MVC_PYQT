from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon

from src.utils import resource_path

UI_PATH = resource_path("src/views/main_gui_mvc_motoristas.ui")  # Path do ui


class ViewMain(QMainWindow):
    def __init__(self, controller: object) -> None:
        super(ViewMain, self).__init__()
        uic.loadUi(UI_PATH, self)
        self.setWindowIcon(QIcon(resource_path("src/midia/logo/icone.ico")))
        self.controller = controller

        # Tab search by name
        self.btn_name_search = self.findChild(QPushButton, "btn_name_search")
        self.lineedit_name_search = self.findChild(QLineEdit, "lineedit_name_search")
        self.textedit_name_search = self.findChild(QTextEdit, "textedit_name_search")

        # Tab search by plate
        self.btn_plate_search = self.findChild(QPushButton, "btn_plate_search")
        self.lineedit_plate_search = self.findChild(QLineEdit, "lineedit_plate_search")
        self.textedit_plate_search = self.findChild(QTextEdit, "textedit_plate_search")

        # Tab register
        self.btn_driver_register = self.findChild(QPushButton, "btn_driver_register")
        self.lineedit_name_register = self.findChild(
            QLineEdit, "lineedit_name_register"
        )
        self.lineedit_plate_register = self.findChild(
            QLineEdit, "lineedit_plate_register"
        )
        self.lineedit_type_register = self.findChild(
            QLineEdit, "lineedit_type_register"
        )
        self.label_result_register = self.findChild(QLabel, "label_result_register")

        # Tab delete
        self.btn_delete_delete = self.findChild(QPushButton, "btn_delete_delete")
        self.lineedit_name_delete = self.findChild(QLineEdit, "lineedit_name_delete")
        self.btn_verify_delete = self.findChild(QPushButton, "btn_verify_delete")
        self.label_result_delete = self.findChild(QLabel, "label_result_delete")

        self.btn_delete_delete.setEnabled(False)

        # Button connection
        self.btn_name_search.clicked.connect(
            lambda: self.controller.search_by_name(self.lineedit_name_search.text())
        )
        self.btn_plate_search.clicked.connect(
            lambda: self.controller.search_by_plate(self.lineedit_plate_search.text())
        )
        self.btn_driver_register.clicked.connect(
            lambda: self.controller.register_driver(
                self.lineedit_name_register.text(),
                self.lineedit_plate_register.text(),
                self.lineedit_type_register.text(),
            )
        )
        self.btn_verify_delete.clicked.connect(
            lambda: self.controller.verify_delete(self.lineedit_name_delete.text())
        )
        self.btn_delete_delete.clicked.connect(
            lambda: self.controller.delete_driver(self.lineedit_name_delete.text())
        )
