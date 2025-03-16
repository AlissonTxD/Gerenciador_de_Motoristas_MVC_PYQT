from typing import Dict, List
import json

PATH = "motoristas.json"


class DriversRepository:
    def __init__(self) -> None:
        try:
            self.data = self.__open_json()
        except:
            with open(PATH, "w") as fp:
                json.dump([], fp)
            self.data = self.__open_json()

    def get_data(self) -> List:
        self.__reload_data()
        return self.data

    def register_in_json(self, driver: Dict) -> None:
        self.__reload_data()
        self.data.append(driver)
        self.save_json(self.data)

    def save_json(self, obj: List) -> None:
        sorted_drivers_list = sorted(obj, key=lambda motorista: motorista["name"])
        with open(PATH, "w") as fp:
            json.dump(sorted_drivers_list, fp, indent=2)

    def __reload_data(self) -> None:
        self.data = self.__open_json()

    def __open_json(self) -> list:
        with open(PATH, "r") as fp:
            var = json.load(fp)
            return var
