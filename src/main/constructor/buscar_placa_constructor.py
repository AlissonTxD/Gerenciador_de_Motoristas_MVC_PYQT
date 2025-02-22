from src.views.buscar_placa_view import BuscadorDePessoasPorPlaca

def buscar_placa_constructor():
    buscar_placa = BuscadorDePessoasPorPlaca()
    informacao_buscar_placa = buscar_placa.buscar_placa_view()
    #enviar para controler