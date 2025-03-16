from src.test.sample_list import sample_list
from src.models.model_delete import ModelDelete

model = ModelDelete()


def test_verify_delete():
    response = model.verify_delete("CARLOS", sample_list)

    assert response["success"] == True
    assert response["driver"] == {'name': 'CARLOS', 'plate': 'ABC1234', 'type': 'FRETEIRO'}

def test_verify_delete_name_not_found():
    response = model.verify_delete("genivaldo", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Com Esse Exato Nome Não Encontrado"

def test_verify_delete_name_empty():
    response = model.verify_delete("", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"

def test_delete_driver():
    response = model.delete_driver("ROBERTO", sample_list)
    assert response["success"] == True
    assert len(response["data"]) == 3

def test_delete_driver_name_not_found():
    response = model.delete_driver("genivaldo", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Motorista Com Esse Exato Nome Não Encontrado"

def test_delete_driver_name_empty():
    response = model.delete_driver("", sample_list)
    assert response["success"] == False
    assert response["error"] == "Erro: Campo Vazio!"
