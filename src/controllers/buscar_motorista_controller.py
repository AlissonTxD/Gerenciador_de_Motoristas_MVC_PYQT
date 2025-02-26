from typing import Dict
from src.models.repository.motoristas_repository import RepositorioMotoristas

class BuscarMotorista:
    def Buscar(self, informacao_busca:dict) -> Dict:
        try:
            self.__validate_fields(informacao_busca)
            motoristas = self.__procurar_motorista(informacao_busca)
            response = self.__format_response(motoristas)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validate_fields(self,informacao_busca: Dict):
        if informacao_busca["tipo"] == "name" and not isinstance(informacao_busca["information"],str):
            raise Exception("Campo Nome Invalido!")
        elif informacao_busca["tipo"] == "plate" and not isinstance(informacao_busca["information"],str):
            raise Exception("Campo Placa Invalido!")
        
    def __procurar_motorista(self, informacao_busca: Dict) -> Dict:
        repositorio = RepositorioMotoristas()
        resposta = repositorio.procurar_motorista(informacao_busca)
        if resposta:
            return resposta
        else:
            raise Exception('Motorista Não Encontrado')

    def __format_response(self, motorista: any) -> Dict:
        formated_motoristas = []
        ctd = 1
        for motorista in motorista:
            form = {
                "name": motorista["name"],
                "plate": motorista["plate"],
                "type": motorista["type"],
                "num": ctd
            }
            formated_motoristas.append(form)
            ctd += 1
        return formated_motoristas
        