from src.views.view_main import ViewMain

class ControllerMain:
    def __init__(self, view: ViewMain):
        self.view = view

    def search_by_name(self,name: str):
        print(f"procurando por nome: {name}")
        self.view.lineedit_name_search.setText("")
        #enviar para o model de procurar

    def search_by_plate(self, plate: str):
        print(f"procurando por placa: {plate}")
        self.view.lineedit_plate_search.setText("")
        #enviar para o model de procurar

    def register_driver(self, name: str, plate: str, type: str):
        self.view.label_register.setText(f"Registrando motorista: {name} placa: {plate} tipo: {type}")
        self.view.lineedit_name_register.setText("")
        self.view.lineedit_plate_register.setText("")
        self.view.lineedit_type_register.setText("")
        #enviar para o model de registrar

    def verify_delete(self, name: str):
        print(f"verificando se pode deletar: {name}")
        #enviar para o model de verificar
        #retorna se foi encontrado ou nao
        self.view.label_result_delete.setText(name)
        self.view.btn_delete_delete.setEnabled(True)

    def delete_driver(self, name: str):
        print(f"deletando motorista: {name}")
        self.view.btn_delete_delete.setEnabled(False)
        self.view.label_result_delete.setText("")
    

    