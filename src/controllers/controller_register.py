
from src.models.repository import DriversRepository
from src.views.view_main import ViewMain
from src.models.model_register import ModelRegister

def controller_register(name: str, plate: str, type: str):
    repository = DriversRepository()
    view = ViewMain()
    data = repository.get_data()
    register_model = ModelRegister()
    response = register_model.register(name, plate, type, data)
    if response["success"]:
        repository.register_in_json(response["driver"])
        view.label_result_register.setText(
            f"Motorista Cadastrado!\nNome: {response["driver"]["name"]}\nPlaca: {response["driver"]["plate"]}\nTipo: {response["driver"]["type"]}"
        )
        view.lineedit_name_register.setText("")
        view.lineedit_plate_register.setText("")
        view.lineedit_type_register.setText("")
    else:
        view.label_result_register.setText(response["error"])