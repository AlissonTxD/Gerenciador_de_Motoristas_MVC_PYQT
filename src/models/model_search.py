from typing import Dict


class ModelDriverSearch:
    def search(self, value: str, data: list, criteria: str) -> Dict:
        try:
            self.__validate_field(value)
            drivers = self.__searching(value, data, criteria)
            response = self.__format_response(drivers)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_field(self, field: str) -> None:
        is_empty = len(field) < 1
        if is_empty:
            raise Exception("Campo Vazio!")

    def __searching(self, value: str, data: list, criteria: str) -> list:
        if value.upper() == "ALL":
            return data
        driver_list = []
        if not data:
            return driver_list
        for driver in data:
            if value.upper() in driver[criteria].upper():
                driver_list.append(driver)
        if driver_list:
            return driver_list
        else:
            raise Exception("Motorista Não Encontrado")

    def __format_response(self, drivers: list) -> str:
        formatted_drivers = ""
        count = 1
        if not drivers:
            return "Nenhum Motorista Cadastrado"
        for driver in drivers:
            text = f"Nº{count} Nome: {driver['name']}, Placa: {driver['plate']}, Tipo: {driver['type']}\n"
            formatted_drivers += text
            count += 1
        return formatted_drivers
