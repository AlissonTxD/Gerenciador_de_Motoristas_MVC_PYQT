from test.sample_list import sample_list_returner
from src.models.model_delete import ModelDelete

model = ModelDelete()
sample_list = sample_list_returner()


def test_verify_delete():
    response = model.verify_for_delete("driver001", sample_list)

    assert response["success"] == True
    assert response["driver"] == {
        "name": "DRIVER001",
        "plate": "PLATE01",
        "type": "TYPE01",
    }


def test_verify_delete_name_not_found():
    response = model.verify_for_delete("driver005", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Com Esse Exato Nome Não Encontrado"


def test_verify_delete_name_empty():
    response = model.verify_for_delete("", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"
