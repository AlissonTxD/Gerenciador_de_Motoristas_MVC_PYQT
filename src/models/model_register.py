from typing import Dict


class ModelRegister:
    def register(self, name: str, plate: str, type: str, data: list) -> Dict:
        """Gives the data to the methods and returns the response

        Args:
            name (str): Name of the driver to be registered
            plate (str): Plate of the drivers vehicle to be registered
            type (str): Type of the driver to be registered
            data (list): Data of the actual registered drivers

        Returns:
            Dict: Dictionary containing the driver data formated
        """
        try:
            self.__validate_fields(name, plate, type)
            driver = self.__format_response(name, plate, type)
            self.__verify_availability(driver, data)
            return {"success": True, "driver": driver}
        except Exception as exception:
            return {"success": False, "error": f"Erro: {str(exception)}"}

    def __validate_fields(self, name: str, plate: str, type: str) -> None:
        """Checks whether the values ​​meet the requirements

        Args:
            name (str): Name of the driver to be registered
            plate (str): Plate of the drivers vehicle to be registered
            type (str): Type of the driver to be registered

        Raises:
            Exception: If the name field is empty raise name fiel empty
            Exception: If the plate field is not 7 (Base plate size from brazilian vehicles) raise plate fiel wrong
            Exception: If the type field is empty raise plate fiel empty
        """
        name_is_empty = len(name) < 1
        plate_is_invalid = len(plate) != 7
        type_is_empty = len(type) < 1
        if name_is_empty:
            raise Exception("Campo Nome Vazio!")
        if plate_is_invalid:
            raise Exception("Placa Inválida!")
        if type_is_empty:
            raise Exception("Campo Tipo Vazio!")

    def __format_response(self, name: str, plate: str, type: str) -> Dict:
        """Format the data to be inserted in the database

        Args:
            name (str): Name of the driver to be registered
            plate (str): Plate of the drivers vehicle to be registered
            type (str): Type of the driver to be registered

        Returns:
            Dict: Formated dict as the database pattern
        """
        return {"name": name.upper(), "plate": plate.upper(), "type": type.upper()}

    def __verify_availability(self, information: dict, data: list) -> None:
        """Checks if the driver data to be registered isnt already in the database

        Args:
            information (dict): driver to be registered
            data (list): Data of the actual registered drivers

        Raises:
            Exception: get the data of the driver who is already registered with that name
            Exception: get the data of the driver who is already registered with that plate
        """
        for driver in data:
            if driver["name"] == information["name"]:
                raise Exception(
                    f"Este Nome Já Esta Cadastrado\nNome: {driver['name']}\nPlaca: {driver['plate']}"
                )
            elif driver["plate"] == information["plate"]:
                raise Exception(
                    f"Esta Placa Já Esta Cadastrada\nNome: {driver['name']}\nPlaca: {driver['plate']}"
                )
