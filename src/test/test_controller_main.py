from typing import List

from src.controllers import ControllerMain
from src.test.sample_list import sample_list_returner

sample_list = sample_list_returner()


class MockWidgets:
    def __init__(self) -> None:
        self.__text = "user input"

    def setText(self, text) -> None:
        self.__text = text

    def text(self) -> str:
        return self.__text


class MockLineEdit(MockWidgets):
    pass


class MockTextedit(MockWidgets):
    pass


class MockLabel(MockWidgets):
    pass


class MockPushButton(MockWidgets):
    def __init__(self):
        super().__init__()
        self.status = False

    def setEnabled(self, bool: bool) -> None:
        self.status = bool


class MockView:
    def __init__(self):
        self.lineedit_name_search = MockLineEdit()
        self.textedit_name_search = MockTextedit()
        self.textedit_plate_search = MockTextedit()
        self.lineedit_plate_search = MockLineEdit()
        self.label_result_register = MockLabel()
        self.lineedit_name_register = MockLineEdit()
        self.lineedit_plate_register = MockLineEdit()
        self.lineedit_type_register = MockLineEdit()
        self.label_result_delete = MockLabel()
        self.btn_delete_delete = MockPushButton()
        self.lineedit_name_delete = MockLineEdit()


class MockRepository:
    def get_data(self) -> List:
        return sample_list

    def register_in_json(self, driver: dict) -> None:
        pass

    def save_json(self, obj: List) -> None:
        pass


view = MockView()
controller = ControllerMain(view)
controller.repository = MockRepository()


def test_controller_main_search_by_name():
    controller.search_by_name("carlos")
    assert view.lineedit_name_search.text() == ""
    assert (
        view.textedit_name_search.text()
        == "Nº1 Nome: CARLOS, Placa: ABC1234, Tipo: FRETEIRO\n"
    )


def test_controller_main_search_by_name_empty():
    controller.search_by_name("")
    assert view.lineedit_name_search.text() == ""
    assert view.textedit_name_search.text() == "Erro: Campo Vazio!"


def test_controller_main_search_by_name_not_found():
    controller.search_by_name("genivaldo")
    assert view.lineedit_name_search.text() == ""
    assert view.textedit_name_search.text() == "Erro: Motorista Não Encontrado"


def test_controller_main_search_by_plate():
    controller.search_by_plate("abc1234")
    assert view.lineedit_plate_search.text() == ""
    assert (
        view.textedit_plate_search.text()
        == "Nº1 Nome: CARLOS, Placa: ABC1234, Tipo: FRETEIRO\n"
    )


def test_controller_main_search_by_plate_empty():
    controller.search_by_plate("")
    assert view.lineedit_plate_search.text() == ""
    assert view.textedit_plate_search.text() == "Erro: Campo Vazio!"


def test_controller_main_search_by_plate_not_found():
    controller.search_by_plate("kjy9j12")
    assert view.lineedit_plate_search.text() == ""
    assert view.textedit_plate_search.text() == "Erro: Motorista Não Encontrado"


def test_register_driver():
    controller.register_driver("genivaldo", "abc1d23", "freteiro")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert (
        view.label_result_register.text()
        == "Motorista Cadastrado!\nNome: GENIVALDO\nPlaca: ABC1D23\nTipo: FRETEIRO"
    )


def test_register_driver_name_empty():
    controller.register_driver("", "abc1d23", "freteiro")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert view.label_result_register.text() == "Erro: Campo Nome Vazio!"


def teste_register_driver_plate_invalid():
    controller.register_driver("genivaldo", "abc1234d", "freteiro")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert view.label_result_register.text() == "Erro: Placa Inválida!"


def test_register_driver_type_empty():
    controller.register_driver("genivaldo", "abc4312", "")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert view.label_result_register.text() == "Erro: Campo Tipo Vazio!"


def test_register_driver_name_already_used():
    controller.register_driver("mariana", "abc1d34", "ceramica")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert (
        view.label_result_register.text()
        == "Erro: Este Nome Já Esta Cadastrado\nNome: MARIANA\nPlaca: DEF5678"
    )


def test_register_driver_plate_already_used():
    controller.register_driver("genivaldo", "ksnuimn", "freteiro")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert (
        view.label_result_register.text()
        == "Erro: Esta Placa Já Esta Cadastrada\nNome: TESTNALDO\nPlaca: KSNUIMN"
    )


def test_verify_delete():
    controller.verify_delete("carlos")
    assert (
        view.label_result_delete.text()
        == "Motorista Encontrado!\nNome: CARLOS\nPlaca: ABC1234\nTipo: FRETEIRO"
    )
    assert view.btn_delete_delete.status == True
    view.btn_delete_delete.status = False


def test_verify_delete_empty():
    controller.verify_delete("")
    assert view.label_result_delete.text() == "Erro: Campo Vazio!"
    assert view.btn_delete_delete.status == False


def test_verify_delete_driver_not_found():
    controller.verify_delete("non-existent")
    assert (
        view.label_result_delete.text()
        == "Erro: Motorista Com Esse Exato Nome Não Encontrado"
    )
    assert view.btn_delete_delete.status == False


def test_delete():
    controller.delete_driver("carlos")
    assert view.label_result_delete.text() == "Motorista Deletado!"
    assert view.btn_delete_delete.status == False
    assert view.lineedit_name_delete.text() == ""


def test_delete_empty():
    controller.delete_driver("")
    assert view.label_result_delete.text() == "Erro: Campo Vazio!"
    assert view.btn_delete_delete.status == False


def test_delete_not_found():
    controller.delete_driver("non-existent")
    assert (
        view.label_result_delete.text()
        == "Erro: Motorista Com Esse Exato Nome Não Encontrado"
    )
    assert view.btn_delete_delete.status == False
