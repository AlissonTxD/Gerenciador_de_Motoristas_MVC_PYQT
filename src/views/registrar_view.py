from typing import Dict
import os

class RegistradorDePessoasView:
    def registrar_pessoa_view(self) -> Dict:
        os.system("cls||clear")

        print("Cadastrar Novo Motorista \n\n")
        nome = input("Nome do motorista ser registrado: ")
        placa = (input("Placa a ser registrada: "))
        tipo = input("Tipo do Motorista: ")

        nova_informacao = {
            "nome": nome,"placa":placa,"tipo":tipo
        }
        return nova_informacao

    def registro_concluido(self, message: Dict)-> None:
        os.system("cls||clear")
        mensagem_concluido = f"""
            Registro Concluido Com Sucesso!
            Tipo: {message["type"]}
            Registro: {message["count"]}
            Infos:
                Nome: {message["attributes"]["nome"]} 
                Placa: {message["attributes"]["placa"]} 
                Tipo: {message["attributes"]["tipo"]}
        """
        print(mensagem_concluido)

    def registro_falhou(self, error: str) -> None :
        os.system("cls||clear")

        mensagem_falha = f"""
            Falha ao cadastar motorista!

            Erro: { error }
        """
        print(mensagem_falha)