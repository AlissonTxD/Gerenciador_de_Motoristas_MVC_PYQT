from typing import Dict
import os

class BuscadorMotoristaNome:
    def buscar_motorista_view(self,tipo) -> Dict:
        os.system("cls||clear")

        if tipo == "name":
            print("Buscar Motorista por Nome\n\n")
            parametro_busca =  input("coloque o nome da pessoa a ser procurada: ")

        if tipo == "plate":
            print("Buscar Motorista por Placa\n\n")
            parametro_busca =  input("coloque a placa a ser procurada: ")
        
        informacao_busca = {
            "information": parametro_busca,
            "tipo": tipo
        }
        return informacao_busca
    
    def buscar_nome_success(self,message:Dict):
        success_message = f"""
            Registro: {message["num"]}
            Infos:
                Nome: {message["name"]}
                Placa: {message["plate"]}
                Tipo: {message["type"]}
            """
        print(success_message)

    def buscar_nome_fail(self, error:str) -> None:
        os.system("cls||clear")
        fail_message =  f"""
            Falha ao encontrar usuario!
            Erro: {error}
        """
        print(fail_message)