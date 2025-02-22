def tela_inicial():
    mensagem = """
        Identificação de Motoristas

        *Busca por Nome - 1
        *Busca por Placa - 2
        *Cadastrar Pessoa - 3
        *Sair - 5
    """
    print(mensagem)
    comando = input("Comando: ")
    return comando