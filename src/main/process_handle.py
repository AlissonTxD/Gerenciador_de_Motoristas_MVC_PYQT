from .constructor.tela_inicial_process import tela_inicial_process
from .constructor.buscar_motorista_constructor import procurador_de_motorista_constructor
from .constructor.registrar_motorista_constructor import registrar_pessoa_constructor
import os
def inciar() -> None:
    while True:
        comando = tela_inicial_process()
        if comando == "1": procurador_de_motorista_constructor("name")
        elif comando == "2": procurador_de_motorista_constructor("plate")
        elif comando == "3": registrar_pessoa_constructor()
        elif comando == "5": exit()
        else:
            os.system("cls||clear")
            print("Comando Não Encontrado\n")