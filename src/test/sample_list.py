sample_list = [
    {"name": "CARLOS", "plate": "ABC1234", "type": "FRETEIRO"},
    {"name": "MARIANA", "plate": "DEF5678", "type": "PARTICULAR"},
    {"name": "ROBERTO", "plate": "GHI9012", "type": "TAXI"},
    {"name": "TESTNALDO", "plate": "KSNUIMN", "type": "TESTADOR"},
]

def sample_list_returner() -> list:
    new_list = []
    for driver in sample_list:
        new_list.append(driver)
    return new_list
    