from typing import Dict

from src.models.model_search import ModelDriverSearch
from test.sample_list import sample_list_returner


model = ModelDriverSearch()
sample_list = sample_list_returner()


def test_search_name_driver001():
    response = model.search("DRIVER001", sample_list, "name")
    assert response["success"] == True
    assert response["message"] == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\n"


def test_search_all():
    response = model.search("all", sample_list, "name")
    assert response["success"] == True
    assert (
        response["message"]
        == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\nNº2 Nome: DRIVER002, Placa: PLATE02, Tipo: TYPE01\nNº3 Nome: DRIVER003, Placa: PLATE03, Tipo: TYPE02\nNº4 Nome: DRIVER004, Placa: PLATE04, Tipo: TYPE03\n"
    )


def test_search_name_driver_non_existent():
    response = model.search("non-existent", sample_list, "name")
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Não Encontrado"


def test_search_name_empty():
    response = model.search("", sample_list, "name")
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"


def test_search_plate_plate_01():
    response = model.search("plate01", sample_list, "plate")
    assert response["success"] == True
    assert response["message"] == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\n"


def test_search_plate_non_existent():
    response = model.search("non-existent", sample_list, "plate")
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Não Encontrado"


def test_search_plate_empty():
    response = model.search("", sample_list, "plate")
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"


def test_search_type_type01():
    response = model.search("type01", sample_list, "type")
    assert response["success"] == True
    assert (
        response["message"]
        == "Nº1 Nome: DRIVER001, Placa: PLATE01, Tipo: TYPE01\nNº2 Nome: DRIVER002, Placa: PLATE02, Tipo: TYPE01\n"
    )


def test_search_type_non_existent():
    response = model.search("non-existent", sample_list, "type")
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Não Encontrado"


def test_search_type_empty():
    response = model.search("", sample_list, "type")
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"
