from src.controllers.buscar_motorista_controller import BuscarMotorista
from src.controllers.registrar_motorista_controller import RegistradorDePessoasController
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QApplication
from PyQt5 import uic
import sys
import time

UI_PATH = "src/views/gui_main.ui"  # Path do ui


class gui_clash(QMainWindow):
    def __init__(self) -> None:
        super(gui_clash, self).__init__()
        uic.loadUi(UI_PATH, self)
        self.buscar_motorista_controller = BuscarMotorista()
        self.registrar_motorista_controller = RegistradorDePessoasController()

        # Definir os widgets
        # Definindo abas
        self.aba_nome = self.tabWidget.widget(0)
        self.aba_placa = self.tabWidget.widget(1)
        self.aba_registro = self.tabWidget.widget(2)

        # Definindo widgets dentro da aba buscar nome
        self.input_name = self.findChild(
            QLineEdit, "input_name")
        self.label_name = self.aba_nome.findChild(
            QLabel, "label_name")
        self.procurar_nome_btn = self.aba_nome.findChild(
            QPushButton, "procurar_nome_btn")
        
        # Definindo widgets dentro da aba placa
        self.input_plate = self.aba_placa.findChild(
            QLineEdit, "input_plate")
        self.label_plate = self.aba_placa.findChild(
            QLabel, "label_plate")
        self.procurar_placa_btn = self.aba_placa.findChild(
            QPushButton, "procurar_placa_btn")
        
        # Definindo widgets dentro da aba registro
        self.input_name_register = self.findChild(
            QLineEdit, "input_name_register")
        self.input_plate_register = self.findChild(
            QLineEdit, "input_plate_register")
        self.input_type_register = self.findChild(
            QLineEdit, "input_type_register")
        self.label_register = self.findChild(
            QLabel, "label_register")
        self.register_btn = self.findChild(
            QPushButton, "register_btn")
        
        # Conectar o botão ao slot
        self.procurar_nome_btn.clicked.connect(
            lambda: self.__procurar_motorista("name", self.input_name, self.label_name))
        self.procurar_placa_btn.clicked.connect(
            lambda: self.__procurar_motorista("plate", self.input_plate, self.label_plate))
        
        self.register_btn.clicked.connect(self.__registrar_motorista)

        self.show()             #INIALIZA A JANELA

    def __procurar_motorista(
            self,
            tipo: str,
            input: QLineEdit,
            label: QLabel) -> None:
        parametro_busca = input.text()
        input.setText("")
        
        informacao_busca = {"information": parametro_busca, "tipo": tipo}
        resposta = self.buscar_motorista_controller.Buscar(informacao_busca)

        if resposta["success"]:
            label.setText(resposta["message"])
        else:
            label.setText(resposta["error"])

    def __registrar_motorista(self) -> None:
        nome = self.input_name_register.text()
        placa = self.input_plate_register.text()
        tipo = self.input_type_register.text()
        self.input_name_register.setText("")
        self.input_plate_register.setText("")
        self.input_type_register.setText("")

        nova_informacao = {"name": nome, "plate": placa, "type": tipo}
        resposta = self.registrar_motorista_controller.registrar(
            nova_informacao)

        if resposta["success"]:
            self.label_register.setText(resposta["message"])
        else:
            self.label_register.setText(resposta["error"])
