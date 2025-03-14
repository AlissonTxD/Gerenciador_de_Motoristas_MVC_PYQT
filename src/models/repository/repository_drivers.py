from typing import Dict
import json
from threading import Thread

from playsound import playsound

from src.utils import resource_path

PATH_AUDIO = resource_path("src/midia/mp3/genivaldo_vagabundo.mp3")
PATH = "motoristas.json"


class DriversRepository:
    def __init__(self) -> None:
        try:
            self.data = self.__open_json()
        except:
            with open(PATH, 'w') as fp:
                json.dump([], fp)
            self.data = self.__open_json()

    def get_data(self):
        self.__reload_data()
        return self.data
    
    def __reload_data(self):
        self.data = self.__open_json()
    
    def register_in_json(self, driver: Dict) -> None:
        self.__reload_data()
        self.data.append(driver)
        self.save_json(self.data)

    def __open_json(self) -> list:
        with open(PATH, "r") as fp:
            var = json.load(fp)
            return var

    def save_json(
            self,
            obj: any) -> None:
        sorted_drivers_list = sorted(obj,key=lambda motorista: motorista["name"])
        with open(PATH, 'w') as fp:
            json.dump(sorted_drivers_list, fp, indent=2)
