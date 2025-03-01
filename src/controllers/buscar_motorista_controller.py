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
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_fields(
            self,
            informacao_busca: Dict) -> None:
        is_name = informacao_busca["tipo"] == "name"
        is_plate = informacao_busca["tipo"] == "plate"
        is_vazio = len(informacao_busca["information"]) < 1
        not_is_string = not isinstance(informacao_busca["information"], str)

        if is_name and not_is_string or is_name and is_vazio:
            raise Exception("Campo Nome Invalido!")
        elif is_plate and not_is_string or is_plate and is_vazio:
            raise Exception("Campo Placa Invalido!")
        
    def __procurar_motorista(
            self,
            informacao_busca: Dict) -> Dict:
        repositorio = RepositorioMotoristas()
        resposta = repositorio.procurar_motorista(informacao_busca)
        if resposta:
            return resposta
        else:
            raise Exception('Motorista Não Encontrado')

    def __format_response(
            self,
            motoristas: any) -> Dict:
        formated_motoristas = ""
        ctd = 1
        
        for motorista in motoristas:
            texto = f"Nº{ctd} Nome: {motorista["name"]}, Placa: {motorista["plate"]}, Tipo: {motorista["type"]}\n"
            formated_motoristas += texto
            ctd += 1
        return formated_motoristas
        