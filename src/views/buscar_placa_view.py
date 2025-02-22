from typing import Dict
import os

class BuscadorDePessoasPorPlaca:
    def buscar_placa_view(self) -> Dict:
        os.system("cls||clear")
        
        print("Buscar Motorista por Placa\n\n")
        placa =  input("coloque a Placa a ser procurada: ")

        informacao_pessoa = {
            "placa": placa
        }
        return informacao_pessoa
