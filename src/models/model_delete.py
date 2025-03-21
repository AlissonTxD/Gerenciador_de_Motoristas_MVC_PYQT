from typing import Dict


class ModelDelete:
    def verify_for_delete(self, name: str, data: list) -> Dict:
        """Gives the data to the methods and returns the response

        Args:
            name (str): Name of the driver to be checked or deleted
            data (list): Data of the actual registered drivers

        Returns:
            Dict: Dictionary containing the driver data formated
        """
        try:
            self.__validate_field(name)
            driver = self.__search_exact_name(name, data)
            return {"success": True, "driver": driver}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_field(self, name: str) -> None:
        """Checks whether the values ​​meet the requirements

        Args:
            name (str): Name of the driver to be checked or deleted

        Raises:
            Exception: If the field is empty raise fiel empty
        """
        is_empty = len(name) < 1
        if is_empty:
            raise Exception("Campo Vazio!")

    def __search_exact_name(self, name: str, data: list) -> Dict:
        """Checks the data if there is a driver with the name

        Args:
            name (str): Exact name of the driver to be checked if is on the data
            data (list): Data of the actual registered drivers

        Raises:
            Exception: If name not found in data raise driver not found

        Returns:
            Dict: Dict with the drivers data
        """
        for driver in data:
            if driver["name"] == name.upper():
                return driver
        raise Exception("Motorista Com Esse Exato Nome Não Encontrado")
