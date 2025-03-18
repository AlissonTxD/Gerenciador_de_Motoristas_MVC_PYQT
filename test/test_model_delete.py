from test.sample_list import sample_list_returner
from src.models.model_delete import ModelDelete

model = ModelDelete()
sample_list = sample_list_returner()


def test_verify_delete():
    response = model.verify_delete("driver001", sample_list)

    assert response["success"] == True
    assert response["driver"] == {
        "name": "DRIVER001",
        "plate": "PLATE01",
        "type": "TYPE01",
    }


def test_verify_delete_name_not_found():
    response = model.verify_delete("driver005", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Com Esse Exato Nome Não Encontrado"


def test_verify_delete_name_empty():
    response = model.verify_delete("", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"


def test_delete_driver():
    data = sample_list_returner()
    response = model.delete_driver("DRIVER001", data)
    assert response["success"] == True
    assert len(response["data"]) == 3


def test_delete_driver_name_not_found():
    response = model.delete_driver("driver005", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Com Esse Exato Nome Não Encontrado"


def test_delete_driver_name_empty():
    response = model.delete_driver("", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"
