from typing import Dict


class ModelDelete:
    def verify_delete(self, name: str, data: list) -> Dict:
        try:
            self.__validate_field(name)
            driver = self.__search_exact_name(name, data)
            return {"success": True, "driver": driver}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def delete_driver(self, name: str, data: list) -> Dict:
        try:
            self.__validate_field(name)
            driver = self.__search_exact_name(name, data)
            return {"success": True, "driver": driver}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_field(self, name: str) -> None:
        is_empty = len(name) < 1
        if is_empty:
            raise Exception("Campo Vazio!")

    def __search_exact_name(self, name: str, data: list) -> Dict:
        for driver in data:
            if driver["name"] == name.upper():
                return driver
        raise Exception("Motorista Com Esse Exato Nome Não Encontrado")
