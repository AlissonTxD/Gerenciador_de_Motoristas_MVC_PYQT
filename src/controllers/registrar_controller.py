from typing import Dict

class RegistradorDePessoasController: 
    def registrar(self, nova_informacao:Dict) -> Dict:
        try:
            self.__validate_fields(nova_informacao)
            #enviar para models
            response = self.__format_response(nova_informacao)
            return {"success": True, "message": response}
        except Exception as ex:
            return {"success": False, "error": str(ex)}

    def __validate_fields(self,nova_informacao) -> None:
        if not isinstance(nova_informacao["nome"],str):
            raise Exception("Campo Nome Incorreto")
        
        if not isinstance(nova_informacao["placa"],str):
            raise Exception("Campo Placa Incorreto")
        
        if not isinstance(nova_informacao["tipo"],str):
            raise Exception("Campo tipo Incorreto")

    def __format_response(self, nova_infomacao: Dict) ->dict:
        return{
            "count":1,
            "type": "Motorista",
            "attributes": nova_infomacao
        }
