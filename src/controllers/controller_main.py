from src.views.view_main import ViewMain
from src.controllers.controller_seach import controller_search
from src.controllers.controller_register import controller_register
from src.controllers.controller_delete import (
    controller_delete_driver,
    controller_verify_delete_driver,
)


class ControllerMain:
    def search(self, criteria: str, value: str) -> None:
        """Directs view data to specific controllers

        Args:
            criteria (str): Search criteria, probably (name, plate, type)
            value (str): Search value
        """
        controller_search(criteria, value)

    def register_driver(self, name: str, plate: str, type: str) -> None:
        """Directs view data to specific controllers

        Args:
            name (str): Name of the driver to be registered
            plate (str): Plate of the drivers vehicle to be registered
            type (str): Type of the driver to be registered
        """
        controller_register(name, plate, type)

    def verify_delete(self, name: str) -> None:
        """Directs view data to specific controllers

        Args:
            name (str): Name of the driver to be check if is in the database
        """
        controller_verify_delete_driver(name)

    def delete_driver(self, name: str) -> None:
        """Directs view data to specific controllers

        Args:
            name (str): Name of the driver to be deleted if is in the database
        """
        controller_delete_driver(name)
