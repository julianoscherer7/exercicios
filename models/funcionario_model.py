from database.gerenciador_banco import GerenciadorBancoDados

class FuncionarioModel:
    def __init__(self):
        self.db = GerenciadorBancoDados(host="localhost", usuario="root", senha="senha", banco="gestao_pessoal")
        self.db.conectar()

    def buscar_por_cpf(self, cpf):
        query = "SELECT * FROM Funcionarios WHERE cpf = %s"
        return self.db.executar_consulta(query, (cpf,))

    def salvar(self, nome, cpf, cargo, departamento, email, data_contratacao):
        query = """
        INSERT INTO Funcionarios (nome, cpf, cargo, departamento, email, data_contratacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (nome, cpf, cargo, departamento, email, data_contratacao)
        return self.db.executar_comando(query, valores)