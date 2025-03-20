from src.views.view_main import ViewMain
from src.controllers.controller_seach import controller_search
from src.controllers.controller_register import controller_register
from src.controllers.controller_delete import (
    controller_delete_driver,
    controller_verify_delete_driver,
)


class ControllerMain:
    def __init__(self, view: ViewMain):
        self.view = view

    def search(self, criteria: str, value: str) -> None:
        controller_search(criteria, value)

    def register_driver(self, name: str, plate: str, type: str) -> None:
        controller_register(name, plate, type)

    def verify_delete(self, name: str) -> None:
        controller_verify_delete_driver(name)

    def delete_driver(self, name: str) -> None:
        controller_delete_driver(name)
