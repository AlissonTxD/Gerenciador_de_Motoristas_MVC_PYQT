from typing import Dict

from test.sample_list import sample_list_returner
from src.models.model_register import ModelRegister

model = ModelRegister()
sample_list = sample_list_returner()


def test_register():
    data = sample_list_returner()
    response = model.register("driver005", "plate05", "type05", data)
    assert response["success"] == True
    assert response["driver"] == {
        "name": "DRIVER005",
        "plate": "PLATE05",
        "type": "TYPE05",
    }


def test_register_name_empty_error():
    response = model.register("", "plate06", "type06", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Nome Vazio!"


def test_register_plate_invalid_error():
    response = model.register("driver006", "plate006", "type06", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Placa Inválida!"


def test_register_type_empty_error():
    response = model.register("driver006", "plate06", "", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Tipo Vazio!"


def test_register_name_already_used():
    response = model.register("driver001", "plate06", "type06", sample_list)
    assert response["success"] == False
    assert (
        response["error"]
        == "Erro: Este Nome Já Esta Cadastrado\nNome: DRIVER001\nPlaca: PLATE01"
    )


def test_register_plate_already_used():
    response = model.register("driver006", "plate01", "type10", sample_list)
    assert response["success"] == False
    assert (
        response["error"]
        == "Erro: Esta Placa Já Esta Cadastrada\nNome: DRIVER001\nPlaca: PLATE01"
    )
