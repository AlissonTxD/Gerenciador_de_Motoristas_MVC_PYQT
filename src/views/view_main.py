from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QTextEdit, QRadioButton
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

        # Tab search
        self.btn_search = self.findChild(QPushButton, "btn_search")
        self.lineedit_search = self.findChild(QLineEdit, "lineedit_search")
        self.textedit_search = self.findChild(QTextEdit, "textedit_search")
        self.radiobtn_name = self.findChild(QRadioButton, "radiobtn_name")
        self.radiobtn_plate = self.findChild(QRadioButton, "radiobtn_plate")
        self.radiobtn_type = self.findChild(QRadioButton, "radiobtn_type")

        self.radiobtn_name.setChecked(True)

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
        self.btn_search.clicked.connect(self.__search_driver)

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

    def __search_driver(self):
        if self.radiobtn_name.isChecked():
            criteria = "name"
        elif self.radiobtn_plate.isChecked():
            criteria = "plate"
        elif self.radiobtn_type.isChecked():
            criteria = "type"
        self.controller.search(criteria, self.lineedit_search.text())