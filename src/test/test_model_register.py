from typing import Dict

from src.test.sample_list import sample_list
from src.models.model_register import ModelRegister

model = ModelRegister()


def test_register():
    response = model.register("genivaldo", "ABC1D23", "freteiro", sample_list)
    assert response["success"] == True
    assert response["driver"] == {
        "name": "GENIVALDO",
        "plate": "ABC1D23",
        "type": "FRETEIRO",
    }


def test_register_name_empty_error():
    response = model.register("", "ABC1D23", "freteiro", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Nome Vazio!"


def test_register_plate_invalid_error():
    response = model.register("genivaldo", "ABC1D234", "freteiro", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Placa Inválida!"


def test_register_type_empty_error():
    response = model.register("genivaldo", "ABC1D23", "", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Tipo Vazio!"


def test_register_name_already_used():
    response = model.register("carlos", "ABC1D23", "freteiro", sample_list)
    assert response["success"] == False
    assert (
        response["error"]
        == "Erro: Este Nome Já Esta Cadastrado\nNome: CARLOS\nPlaca: ABC1234"
    )


def test_register_plate_already_used():
    response = model.register("genivaldo", "ABC1234", "freteiro", sample_list)
    assert response["success"] == False
    assert (
        response["error"]
        == "Erro: Esta Placa Já Esta Cadastrada\nNome: CARLOS\nPlaca: ABC1234"
    )
