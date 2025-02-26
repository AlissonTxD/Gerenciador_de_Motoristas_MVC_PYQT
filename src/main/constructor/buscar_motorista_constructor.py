from src.views.buscar_motorista_view import BuscadorMotoristaNome
from src.controllers.buscar_motorista_controller import BuscarMotorista

def procurador_de_motorista_constructor(tipo:str):
    buscar_motorista_view = BuscadorMotoristaNome()
    buscar_motorista_controller = BuscarMotorista()
    if tipo == "name":
        informacao_busca = buscar_motorista_view.buscar_motorista_view(tipo)
    elif tipo == "plate":
        informacao_busca = buscar_motorista_view.buscar_motorista_view(tipo)
    
    resposta = buscar_motorista_controller.Buscar(informacao_busca)
    
    if resposta["success"]:
        print(f"{len(resposta['message'])} Motorista(s) Encontrado(s)")
        for motorista in resposta["message"]:
            buscar_motorista_view.buscar_nome_success(motorista)
    else:
        buscar_motorista_view.buscar_nome_fail(resposta["error"])