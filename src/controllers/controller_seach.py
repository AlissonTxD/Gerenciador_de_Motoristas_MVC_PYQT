from threading import Thread

from playsound import playsound

from src.models.repository import DriversRepository
from src.models.model_search import ModelDriverSearch
from src.views.view_main import ViewMain
from src.utils import resource_path

MP3_GENIVALDO = resource_path("src/midia/mp3/genivaldo_vagabundo.mp3")


def controller_search(criteria: str, value: str) -> None:
    """Send the data recived from the view and the repository to the model and send the response back to the view

    Args:
        criteria (str): Search criteria, probably (name, plate, type)
        value (str): Search value
    """
    repository = DriversRepository()
    view = ViewMain(None)
    if value.upper() == "GENIVALDO":
        mp3_thread = Thread(target=lambda: playsound(MP3_GENIVALDO), daemon=True)
        mp3_thread.start()
    data = repository.get_json_data()
    search_model = ModelDriverSearch()
    response = search_model.search(value, data, criteria)
    textedit = view.textedit_search
    view.lineedit_search.setText("")
    if response["success"]:
        textedit.setText(response["message"])
    else:
        textedit.setText(response["error"])
