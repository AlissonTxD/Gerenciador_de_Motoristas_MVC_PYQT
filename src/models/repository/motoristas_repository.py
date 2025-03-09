from typing import Dict
import json
from threading import Thread
from playsound import playsound

from src.utils import resource_path

PATH_AUDIO = resource_path("src/midia/mp3/genivaldo_vagabundo.mp3")
PATH = "motoristas.json"


class RepositorioMotoristas:
    def __init__(self) -> None:
        try:
            self.data = self.__open_json()
        except:
            with open(PATH, 'w') as fp:
                json.dump([], fp)
            self.data = self.__open_json()
    def registrar(
            self,
            motorista: Dict) -> None:
        self.data.append(motorista)
        self.__save_json(self.data)

    def procurar_motorista(
            self,
            informacao_busca: str) -> list:
        if informacao_busca["information"].upper() == "ALL":
            return self.data
        if informacao_busca["information"].upper() == "GENIVALDO":
            thread_audio = Thread(target=lambda: playsound(PATH_AUDIO), daemon=True)
            thread_audio.start()
        
        motoristas_encontrados = []

        for motorista in self.data:
            if informacao_busca["information"].upper() in motorista[informacao_busca["tipo"]]:
                motoristas_encontrados.append(motorista)
                
        if motoristas_encontrados:
            return motoristas_encontrados
        else:
            return None

    def verificar_disponibilidade(
            self,
            informacao: Dict) -> Dict:
        for motorista in self.data:
            if motorista["name"] == informacao["name"]:
                return {"exists": True, "message": f"Este Nome Já Esta Cadastrado\nNome: {motorista["name"]}\nPlaca: {motorista["plate"]}"}
            elif motorista["plate"] == informacao["plate"]:
                return {"exists": True, "message": f"Esta Placa Já Esta Cadastrada\nNome: {motorista["name"]}\nPlaca: {motorista["plate"]}"}
        return {"exists": False}

    def __open_json(self) -> list:
        with open(PATH, "r") as fp:
            var = json.load(fp)
            return var

    def __save_json(
            self,
            obj: any) -> None:
        lista_organizada = sorted(obj,key=lambda motorista: motorista["name"])
        with open(PATH, 'w') as fp:
            json.dump(lista_organizada, fp, indent=2)
