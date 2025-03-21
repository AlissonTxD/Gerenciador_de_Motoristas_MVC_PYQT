from src.models.model_delete import ModelDelete
from src.models.repository import DriversRepository
from src.views.view_main import ViewMain

repository = DriversRepository()


def controller_verify_delete_driver(name: str) -> None:
    """Send the data recived from the view and the repository to the model and send the response back to the view

    Args:
        name (str): Name of the driver that will be checked
    """
    view = ViewMain()
    data = repository.get_json_data()
    model_delete = ModelDelete()
    response = model_delete.verify_for_delete(name, data)
    if response["success"]:
        view.label_result_delete.setText(
            f"Motorista Encontrado!\nNome: {response["driver"]["name"]}\nPlaca: {response["driver"]["plate"]}\nTipo: {response["driver"]["type"]}"
        )
        view.btn_delete_delete.setEnabled(True)
    else:
        view.label_result_delete.setText(response["error"])


def controller_delete_driver(name: str) -> None:
    """Send the data recived from the view and the repository to the model and send the response back to the view

    Args:
        name (str): Name of the driver that will be deleted
    """
    view = ViewMain()
    data = repository.get_json_data()
    model_delete = ModelDelete()
    response = model_delete.verify_for_delete(name, data)
    if response["success"]:
        repository.delete_in_json(response["driver"])
        view.label_result_delete.setText("Motorista Deletado!")
        view.btn_delete_delete.setEnabled(False)
        view.lineedit_name_delete.setText("")
    else:
        view.label_result_delete.setText(response["error"])
        view.btn_delete_delete.setEnabled(False)
