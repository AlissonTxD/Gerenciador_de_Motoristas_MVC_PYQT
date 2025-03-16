from typing import Dict

from src.models.model_search import ModelDriverSearch
from src.test.sample_list import sample_list


model = ModelDriverSearch()


def test_search_name():
    response = model.search("TESTNALDO", sample_list, "name")
    assert response["success"] == True
    assert (
        response["message"] == "Nº1 Nome: TESTNALDO, Placa: KSNUIMN, Tipo: TESTADOR\n"
    )


def test_search_driver_not_found():
    response = model.search("genivaldo", sample_list, "name")
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Não Encontrado"


def test_search_empty_name_field():
    response = model.search("", sample_list, "name")
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"


def test_search_plate():
    response = model.search("KSNUIMN", sample_list, "plate")
    assert response["success"] == True
    assert (
        response["message"] == "Nº1 Nome: TESTNALDO, Placa: KSNUIMN, Tipo: TESTADOR\n"
    )


def test_search_plate_not_found():
    response = model.search("ABC1D23", sample_list, "plate")
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Não Encontrado"


def test_search_empty_plate_field():
    response = model.search("", sample_list, "plate")
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"
