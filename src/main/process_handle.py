from .constructor.tela_inicial_process import tela_inicial_process
from .constructor.buscar_nome_constructor import buscar_nome_constructor
from .constructor.buscar_placa_constructor import buscar_placa_constructor
from .constructor.registrar_constructor import registrar_pessoa

def inciar() -> None:
    while True:
        comando = tela_inicial_process()
        if comando == "1": buscar_nome_constructor()
        elif comando == "2": buscar_placa_constructor()
        elif comando == "3": registrar_pessoa()
        elif comando == "5": exit()
        else: print("Comando Não Encontrado")