from typing import Dict
from src.models.repository.motoristas_repository import RepositorioMotoristas

class RegistradorDePessoasController: 
    def registrar(self, nova_informacao:Dict) -> Dict:
        try:
            self.__validate_fields(nova_informacao)
            informacao_formatada = self.__formatar(nova_informacao)
            self.__verificar_disponibilidade(informacao_formatada)
            self.__registrar(informacao_formatada)
            response = self.__format_response(informacao_formatada)
            return {"success": True, "message": response}
        except Exception as ex:
            return {"success": False, "error": f"Erro: {str(ex)}"}

    def __validate_fields(self,nova_informacao) -> None:
        if not isinstance(nova_informacao["name"],str) or len(nova_informacao["name"]) < 1:
            raise Exception("Campo Nome Incorreto")
        
        if not isinstance(nova_informacao["plate"],str) or len(nova_informacao["plate"]) != 7:
            raise Exception("Campo Placa Incorreto")
        
        if not isinstance(nova_informacao["type"],str) or len(nova_informacao["type"]) < 1:
            raise Exception("Campo tipo Incorreto")

    def __formatar(self, informacao: Dict) -> Dict:
        nome = str(informacao["name"]).upper()
        placa = str(informacao["plate"]).upper()
        tipo = str(informacao["type"]).upper()
        return {"name": nome, "plate": placa, "type": tipo}

    def __verificar_disponibilidade(self,nova_informacao):
        repositorio = RepositorioMotoristas()
        resultado = repositorio.verificar_disponibilidade(nova_informacao)
        if resultado["exists"]:
            raise Exception(resultado["message"])

    def __registrar(self, motorista : Dict):
        repositorio = RepositorioMotoristas()
        repositorio.registrar(motorista)

    def __format_response(self, nova_infomacao: Dict) -> str:
        response = f"""
            Motorista Cadastrado Com Sucesso
            Infos:
            Nome: {nova_infomacao["name"]}
            Placa: {nova_infomacao["plate"]}
            Tipo: {nova_infomacao["type"]}
            """
        return response
    

