from src.views.view_main import ViewMain
from typing import Dict

class ControllerMain:
    def __init__(self, view: ViewMain):
        self.view = view

    def search_by_name(self,name: str):
        print(f"procurando por nome: {name}")
        self.view.lineedit_name_search.setText("")
        #enviar para o model de procurar