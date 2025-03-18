from typing import List
from src.models.repository.model_repository_drivers import DriversRepository

model = DriversRepository()


def test_get_data():
    response = model.get_data()
    assert isinstance(response, List)
