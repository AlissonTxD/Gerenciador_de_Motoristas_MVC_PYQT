sample_list = [
    {"name": "DRIVER001", "plate": "PLATE01", "type": "TYPE01"},
    {"name": "DRIVER002", "plate": "PLATE02", "type": "TYPE01"},
    {"name": "DRIVER003", "plate": "PLATE03", "type": "TYPE02"},
    {"name": "DRIVER004", "plate": "PLATE04", "type": "TYPE03"},
]

def sample_list_returner() -> list:
    new_list = []
    for driver in sample_list:
        new_list.append(driver)
    return new_list
    