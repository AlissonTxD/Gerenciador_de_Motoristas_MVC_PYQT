from typing import Dict


class ModelRegister:
    def register(self, name: str, plate: str, type: str, data: list) -> Dict:
        try:
            self.__validate_fields(name, plate, type)
            driver = self.__format_response(name, plate, type)
            self.__verify_availability(driver, data)
            return {"success": True, "driver": driver}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_fields(self, name: str, plate: str, type: str) -> None:
        name_is_empty = len(name) < 1
        plate_is_invalid = len(plate) < 1 or len(plate) != 7
        type_is_empty = len(type) < 1
        if name_is_empty:
            raise Exception("Campo Nome Vazio!")
        if plate_is_invalid:
            raise Exception("Placa Inválida!")
        if type_is_empty:
            raise Exception("Campo Tipo Vazio!")

    def __format_response(self, name: str, plate: str, type: str) -> Dict:
        return {"name": name.upper(), "plate": plate.upper(), "type": type.upper()}

    def __verify_availability(self, information: dict, data: list) -> None:
        for driver in data:
            if driver["name"] == information["name"]:
                raise Exception(
                    f"Este Nome Já Esta Cadastrado\nNome: {driver['name']}\nPlaca: {driver['plate']}"
                )
            elif driver["plate"] == information["plate"]:
                raise Exception(
                    f"Esta Placa Já Esta Cadastrada\nNome: {driver['name']}\nPlaca: {driver['plate']}"
                )
