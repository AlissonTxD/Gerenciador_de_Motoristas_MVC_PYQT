from typing import List

from src.controllers import ControllerMain
from test.sample_list import sample_list_returner

sample_list = sample_list_returner()


class MockWidget:
    def __init__(self) -> None:
        self.__text = "user input"
        self.status = False

    def setText(self, text) -> None:
        self.__text = text

    def text(self) -> str:
        return self.__text

    def setEnabled(self, bool: bool) -> None:
        self.status = bool


class MockView:
    def __init__(self):
        self.reload()

    def reload(self):
        self.lineedit_search = MockWidget()
        self.textedit_search = MockWidget()
        self.label_result_register = MockWidget()
        self.lineedit_name_register = MockWidget()
        self.lineedit_plate_register = MockWidget()
        self.lineedit_type_register = MockWidget()
        self.label_result_delete = MockWidget()
        self.btn_delete_delete = MockWidget()
        self.lineedit_name_delete = MockWidget()


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


def test_controller_main_search_by_name_driver001():
    controller.search("name", "driver001")
    assert view.lineedit_search.text() == ""
    assert (
        view.textedit_search.text()
        == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\n"
    )


def test_controller_main_search_by_name_empty():
    controller.search("name", "")
    assert view.lineedit_search.text() == ""
    assert view.textedit_search.text() == "Erro: Campo Vazio!"


def test_controller_main_search_by_name_not_found():
    controller.search("name", "non-existent")
    assert view.lineedit_search.text() == ""
    assert view.textedit_search.text() == "Erro: Motorista Não Encontrado"


def test_controller_main_search_by_plate_plate01():
    controller.search("plate", "plate01")
    assert view.lineedit_search.text() == ""
    assert (
        view.textedit_search.text()
        == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\n"
    )


def test_controller_main_search_by_plate_empty():
    controller.search("plate", "")
    assert view.lineedit_search.text() == ""
    assert view.textedit_search.text() == "Erro: Campo Vazio!"


def test_controller_main_search_by_plate_not_found():
    controller.search("plate", "kjy9j12")
    assert view.lineedit_search.text() == ""
    assert view.textedit_search.text() == "Erro: Motorista Não Encontrado"


def test_controller_main_register_driver():
    controller.register_driver("driver005", "plate05", "type05")
    assert view.lineedit_name_register.text() == ""
    assert view.lineedit_plate_register.text() == ""
    assert view.lineedit_type_register.text() == ""
    assert (
        view.label_result_register.text()
        == "Motorista Cadastrado!\nNome: DRIVER005\nPlaca: PLATE05\nTipo: TYPE05"
    )
    view.reload()


def test_controller_main_register_driver_name_empty():
    controller.register_driver("", "plate06", "type06")
    assert view.lineedit_name_register.text() == "user input"
    assert view.lineedit_plate_register.text() == "user input"
    assert view.lineedit_type_register.text() == "user input"
    assert view.label_result_register.text() == "Erro: Campo Nome Vazio!"


def teste_controller_main_register_driver_plate_invalid():
    controller.register_driver("driver010", "plate001", "type10")
    assert view.lineedit_name_register.text() == "user input"
    assert view.lineedit_plate_register.text() == "user input"
    assert view.lineedit_type_register.text() == "user input"
    assert view.label_result_register.text() == "Erro: Placa Inválida!"


def test_controller_main_register_driver_type_empty():
    controller.register_driver("genivaldo", "abc4312", "")
    assert view.lineedit_name_register.text() == "user input"
    assert view.lineedit_plate_register.text() == "user input"
    assert view.lineedit_type_register.text() == "user input"
    assert view.label_result_register.text() == "Erro: Campo Tipo Vazio!"


def test_controller_main_register_driver_name_already_used():
    controller.register_driver("DRIVER001", "plate66", "type66")
    assert view.lineedit_name_register.text() == "user input"
    assert view.lineedit_plate_register.text() == "user input"
    assert view.lineedit_type_register.text() == "user input"
    assert (
        view.label_result_register.text()
        == "Erro: Este Nome Já Esta Cadastrado\nNome: DRIVER001\nPlaca: PLATE01"
    )


def test_controller_main_register_driver_plate_already_used():
    controller.register_driver("driver018", "PLATE01", "type03")
    assert view.lineedit_name_register.text() == "user input"
    assert view.lineedit_plate_register.text() == "user input"
    assert view.lineedit_type_register.text() == "user input"
    assert (
        view.label_result_register.text()
        == "Erro: Esta Placa Já Esta Cadastrada\nNome: DRIVER001\nPlaca: PLATE01"
    )


def test_controller_main_verify_delete():
    controller.verify_delete("driver001")
    assert (
        view.label_result_delete.text()
        == "Motorista Encontrado!\nNome: DRIVER001\nPlaca: PLATE01\nTipo: TYPE01"
    )
    assert view.btn_delete_delete.status == True
    view.btn_delete_delete.status = False


def test_controller_main_verify_delete_empty():
    controller.verify_delete("")
    assert view.label_result_delete.text() == "Erro: Campo Vazio!"
    assert view.btn_delete_delete.status == False


def test_controller_main_verify_delete_driver_not_found():
    controller.verify_delete("non-existent")
    assert (
        view.label_result_delete.text()
        == "Erro: Motorista Com Esse Exato Nome Não Encontrado"
    )
    assert view.btn_delete_delete.status == False


def test_controller_main_delete():
    global sample_list
    controller.delete_driver("DRIVER001")
    assert view.label_result_delete.text() == "Motorista Deletado!"
    assert view.btn_delete_delete.status == False
    assert view.lineedit_name_delete.text() == ""
    sample_list = sample_list_returner()


def test_controller_main_delete_empty():
    controller.delete_driver("")
    assert view.label_result_delete.text() == "Erro: Campo Vazio!"
    assert view.btn_delete_delete.status == False


def test_controller_main_delete_not_found():
    controller.delete_driver("non-existent")
    assert (
        view.label_result_delete.text()
        == "Erro: Motorista Com Esse Exato Nome Não Encontrado"
    )
    assert view.btn_delete_delete.status == False
    assert len(sample_list) == 4
