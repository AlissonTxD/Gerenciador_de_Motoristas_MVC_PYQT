from src.models.repository.model_repository_drivers import DriversRepository

model = DriversRepository()


def test_get_data():
    response = model.get_data()
    assert response == [{'name': 'CARLOS', 'plate': 'ABC1234', 'type': 'FRETEIRO'}, {'name': 'MARIANA', 'plate': 'DEF5678', 'type': 'PARTICULAR'}, {'name': 'ROBERTO', 'plate': 'GHI9012', 'type': 'TAXI'}, {'name': 'TESTNALDO', 'plate': 'KSNUIMN', 'type': 'TESTADOR'}]