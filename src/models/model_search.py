from typing import Dict


class ModelDriverSearch:
    def search(self, value: str, data: list, criteria: str) -> Dict:
        """Gives the data to the methods and returns the response

        Args:
            value (str): Search value
            data (list): Data where the value will be searched
            criteria (str): Search criteria, probably (name, plate, type)

        Returns:
            Dict: Dictionary containing the research data formated
        """
        try:
            self.__validate_field(value)
            drivers = self.__searching(value, data, criteria)
            response = self.__format_response(drivers)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_field(self, field: str) -> None:
        """Checks whether the values ​​meet the requirements

        Args:
            field (str): Value to be checked

        Raises:
            Exception: If the field is empty raise fiel empty
        """
        is_empty = len(field) < 1
        if is_empty:
            raise Exception("Campo Vazio!")

    def __searching(self, value: str, data: list, criteria: str) -> list:
        """Realize a search in the date with the value based on the criteria

        Args:
            value (str): Search value
            data (list): Data where the value will be searched
            criteria (str): Search criteria, probably (name, plate, type)

        Raises:
            Exception: if any driver is found its return driver not found

        Returns:
            list: list with all drivers founds with the value
        """
        if value.upper() == "ALL":
            return data
        driver_list: list = []
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
        """Formats the driver list to be better viewed

        Args:
            drivers (list): list of found drivers

        Returns:
            str: formated string
        """
        formatted_drivers: str = ""
        count = 1
        if not drivers:
            return "Nenhum Motorista Cadastrado"
        for driver in drivers:
            text = f"Nº{count} Nome: {driver['name']}, Placa: {driver['plate']}, Tipo: {driver['type']}\n"
            formatted_drivers += text
            count += 1
        return formatted_drivers
