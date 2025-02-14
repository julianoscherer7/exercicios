from models.funcionario_model import FuncionarioModel

class FuncionarioController:
    def __init__(self):
        self.model = FuncionarioModel()

    def buscar_por_cpf(self, cpf):
        return self.model.buscar_por_cpf(cpf)

    def salvar_funcionario(self, nome, cpf, cargo, departamento, email, data_contratacao):
        return self.model.salvar(nome, cpf, cargo, departamento, email, data_contratacao)