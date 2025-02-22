from src.views.buscar_nome_view import BuscadorDePessoasPorNome

def buscar_nome_constructor():
    buscar_nome = BuscadorDePessoasPorNome()
    informacao_buscar_nome = buscar_nome.buscar_nome_view()
    #enviar para controler