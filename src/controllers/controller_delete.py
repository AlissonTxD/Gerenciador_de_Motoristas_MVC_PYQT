from src.models.model_delete import ModelDelete
from src.models.repository import DriversRepository   
from src.views.view_main import ViewMain

repository = DriversRepository()

def controller_verify_delete(name: str) -> None:
        view = ViewMain()
        data = repository.get_data()
        model_delete = ModelDelete()
        response = model_delete.verify_delete(name, data)
        if response["success"]:
            view.label_result_delete.setText(
                f"Motorista Encontrado!\nNome: {response["driver"]["name"]}\nPlaca: {response["driver"]["plate"]}\nTipo: {response["driver"]["type"]}"
            )
            view.btn_delete_delete.setEnabled(True)
        else:
            view.label_result_delete.setText(response["error"])

def controller_delete(name: str) -> None:
    view = ViewMain()
    data = repository.get_data()
    model_delete = ModelDelete()
    response = model_delete.delete_driver(name, data)
    if response["success"]:
        repository.save_json(response["data"])
        view.label_result_delete.setText("Motorista Deletado!")
        view.btn_delete_delete.setEnabled(False)
        view.lineedit_name_delete.setText("")
    else:
        view.label_result_delete.setText(response["error"])
        view.btn_delete_delete.setEnabled(False)
