from typing import Dict
import json
PATH = "src/models/repository/motoristas.json"
class RepositorioMotoristas:
    def __init__(self):
        self.data = self.__open_json()

    def registrar(self, motorista : Dict) -> None:
        self.data.append(motorista)
        self.__save_json(self.data)

    def procurar_motorista(self, informacao_busca : str) -> list:
        motoristas_encontrados = []
        for motorista in self.data:
            if informacao_busca["information"].upper() in motorista[informacao_busca["tipo"]]:
                motoristas_encontrados.append(motorista)
        if motoristas_encontrados:
            return motoristas_encontrados
        else:
            return None
        
    def verificar_disponibilidade(self, informacao : Dict) -> Dict:
        for motorista in self.data:
            if motorista["name"] == informacao["name"]:
                return {"exists":True,"message": f"Este Nome Já Esta Cadastrado\nNome: {motorista["name"]}\nPlaca: {motorista["plate"]}"}
            elif motorista["plate"] == informacao["plate"]:
                return {"exists":True,"message": f"Esta Placa Já Esta Cadastrada\nNome: {motorista["name"]}\nPlaca: {motorista["plate"]}"}
        return{"exists":False}



    def __open_json(self) -> list:
        with open(PATH, "r") as fp:
            var = json.load(fp)
            return var
        
    def __save_json(self,obj:any) -> None:
        with open(PATH, 'w') as fp:
            json.dump(obj,fp,indent=2)
