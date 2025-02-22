from typing import Dict
import os

class BuscadorDePessoasPorNome:
    def buscar_nome_view(self) -> Dict:
        os.system("cls||clear")
        
        print("Buscar Motorista por Nome\n\n")
        name =  input("coloque o nome da pessoa a ser procurada: ")

        informacao_pessoa = {
            "nome": name
        }
        return informacao_pessoa
