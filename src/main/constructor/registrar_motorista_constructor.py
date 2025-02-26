from src.views.registrar_motorista_view import RegistradorDePessoasView
from src.controllers.registrar_motorista_controller import RegistradorDePessoasController

def registrar_pessoa_constructor():
    registrador_de_pessoa_view = RegistradorDePessoasView()
    registrar_pessoa_controller = RegistradorDePessoasController()
    nova_informacao = registrador_de_pessoa_view.registrar_pessoa_view() 
    response = registrar_pessoa_controller.registrar(nova_informacao)

    if response["success"]:
        registrador_de_pessoa_view.registro_concluido(response["message"])
    else:
        registrador_de_pessoa_view.registro_falhou(response["error"])
