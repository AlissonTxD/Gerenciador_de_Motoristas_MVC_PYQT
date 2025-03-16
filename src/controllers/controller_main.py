from threading import Thread

from playsound import playsound

from src.views.view_main import ViewMain
from src.models.repository import DriversRepository
from src.models.model_search import ModelDriverSearch
from src.models.model_register import ModelRegister
from src.models.model_delete import ModelDelete
from src.utils import resource_path

MP3_GENIVALDO = resource_path("src/midia/mp3/genivaldo_vagabundo.mp3")


class ControllerMain:
    def __init__(self, view: ViewMain):
        self.view = view
        self.repository = DriversRepository()

    def search_by_name(self, name: str) -> None:
        if name.upper() == "GENIVALDO":
            mp3_thread = Thread(target=lambda: playsound(MP3_GENIVALDO), daemon=True)
            mp3_thread.start()
        self.__search("name", name)
        self.view.lineedit_name_search.setText("")

    def search_by_plate(self, plate: str) -> None:
        self.__search("plate", plate)
        self.view.lineedit_plate_search.setText("")

    def __search(self, criteria: str, value: str) -> None:
        data = self.repository.get_data()
        search_model = ModelDriverSearch()
        response = search_model.search(value, data, criteria)

        if criteria == "name":
            textedit = self.view.textedit_name_search
        elif criteria == "plate":
            textedit = self.view.textedit_plate_search

        if response["success"]:
            textedit.setText(response["message"])
        else:
            textedit.setText(response["error"])

    def register_driver(self, name: str, plate: str, type: str) -> None:
        data = self.repository.get_data()
        register_model = ModelRegister()
        response = register_model.register(name, plate, type, data)
        if response["success"]:
            self.repository.register_in_json(response["driver"])
            self.view.label_result_register.setText(
                f"Motorista Cadastrado!\nNome: {response["driver"]["name"]}\nPlaca: {response["driver"]["plate"]}\nTipo: {response["driver"]["type"]}"
            )
            self.view.lineedit_name_register.setText("")
            self.view.lineedit_plate_register.setText("")
            self.view.lineedit_type_register.setText("")
        else:
            self.view.label_result_register.setText(response["error"])

    def verify_delete(self, name: str) -> None:
        data = self.repository.get_data()
        model_delete = ModelDelete()
        response = model_delete.verify_delete(name, data)
        if response["success"]:
            self.view.label_result_delete.setText(
                f"Motorista Encontrado!\nNome: {response["driver"]["name"]}\nPlaca: {response["driver"]["plate"]}\nTipo: {response["driver"]["type"]}"
            )
            self.view.btn_delete_delete.setEnabled(True)
        else:
            self.view.label_result_delete.setText(response["error"])

    def delete_driver(self, name: str) -> None:
        data = self.repository.get_data()
        model_delete = ModelDelete()
        response = model_delete.delete_driver(name, data)
        if response["success"]:
            self.repository.save_json(response["data"])
            self.view.label_result_delete.setText("Motorista Deletado!")
            self.view.btn_delete_delete.setEnabled(False)
            self.view.lineedit_name_delete.setText("")
        else:
            self.view.label_result_delete.setText(response["error"])
