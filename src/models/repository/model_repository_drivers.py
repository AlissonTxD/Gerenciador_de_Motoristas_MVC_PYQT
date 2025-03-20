from typing import Dict, List
import json

PATH = "motoristas.json"


class DriversRepository:
    def __init__(self) -> None:
        self.data = []

    def get_json_data(self, path: str= PATH) -> List:
        self.__load_data(path)
        return self.data

    def register_in_json(self, driver: Dict, path: str= PATH) -> None:
        self.__load_data(path)
        self.data.append(driver)
        self.__save_json(self.data, path)
        
    def delete_in_json(self, driver: Dict, path: str= PATH) -> None:
        self.__load_data(path)
        self.data.remove(driver)
        self.__save_json(self.data, path)
 
    def __save_json(self, obj: List, path: str) -> None:
        sorted_drivers_list = sorted(obj, key=lambda motorista: motorista["name"])
        with open(path, "w") as fp:
            json.dump(sorted_drivers_list, fp, indent=2)

    def __load_data(self, path: str) -> None:
        try:
            self.data = self.__open_json(path)
        except FileNotFoundError:
            with open(path, "w") as fp:
                json.dump([], fp)

    def __open_json(self, path: str) -> list:
        with open(path, "r") as fp:
            var = json.load(fp)
            return var
