from src.controllers import ControllerMain
from src.test.sample_list import sample_list


class MockLineEdit():
    def __init__(self):
        self.__text = ""

    def setText(self, text):
        self.__text = text

    def text(self):
        return self.__text
    
class MockTextedit():
    def __init__(self):
        self.__text = ""
        
    def setText(self, new_text: str):
        self.__text = new_text

    def text(self):
        return self.__text

class MockView():
    def __init__(self):
        self.lineedit_name_search = MockLineEdit()
        self.textedit_name_search = MockTextedit()
        self.textedit_plate_search = MockTextedit()
        self.lineedit_plate_search = MockLineEdit()

class MockRepository():
    def get_data(self):
        return sample_list

view = MockView()
controller = ControllerMain(view)
controller.repository = MockRepository()

def test_controller_main_search_by_name():
    controller.search_by_name("carlos")
    assert view.lineedit_name_search.text() == ""
    assert view.textedit_name_search.text() == "Nº1 Nome: CARLOS, Placa: ABC1234, Tipo: FRETEIRO\n"

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
    assert view.textedit_plate_search.text() == "Nº1 Nome: CARLOS, Placa: ABC1234, Tipo: FRETEIRO\n"

def test_controller_main_search_by_plate_empty():
    controller.search_by_plate("")
    assert view.lineedit_plate_search.text() == ""
    assert view.textedit_plate_search.text() == "Erro: Campo Vazio!"

def test_controller_main_search_by_plate_not_found():
    controller.search_by_plate("kjy9j12")
    assert view.lineedit_plate_search.text() == ""
    assert view.textedit_plate_search.text() == "Erro: Motorista Não Encontrado"
