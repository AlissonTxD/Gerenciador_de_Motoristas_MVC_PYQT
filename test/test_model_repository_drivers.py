from typing import List
import os

from src.models.repository.model_repository_drivers import DriversRepository

model = DriversRepository()
TEST_PATH = "test.json"

if os.path.exists(TEST_PATH):
    os.remove(TEST_PATH)


def test_get_json_data():
    response = model.get_json_data(TEST_PATH)
    assert isinstance(response, List)
    assert response == []


def test_register_in_json():
    model.register_in_json(
        {"name": "DRIVER01", "plate": "PLATE01", "type": "TYPE01"}, TEST_PATH
    )
    response = model.get_json_data(TEST_PATH)
    assert response == [{"name": "DRIVER01", "plate": "PLATE01", "type": "TYPE01"}]


def test_delete_in_json():
    model.delete_in_json({"name": "DRIVER01", "plate": "PLATE01", "type": "TYPE01"},TEST_PATH)
    response = model.get_json_data(TEST_PATH)
    assert response == []
