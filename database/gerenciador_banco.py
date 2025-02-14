import mysql.connector
from mysql.connector import Error

class GerenciadorBancoDados:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            return self.conexao
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def executar_consulta(self, query, params=None):
        try:
            cursor = self.conexao.cursor(dictionary=True)
            cursor.execute(query, params or ())
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        except Error as e:
            print(f"Erro ao executar consulta: {e}")
            return []

    def executar_comando(self, query, params=None):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query, params or ())
            self.conexao.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Erro ao executar comando: {e}")
            return False

    def iniciar_transacao(self):
        try:
            self.conexao.start_transaction()
            return True
        except Error as e:
            print(f"Erro ao iniciar transação: {e}")
            return False

    def confirmar_transacao(self):
        try:
            self.conexao.commit()
            return True
        except Error as e:
            print(f"Erro ao confirmar transação: {e}")
            return False

    def reverter_transacao(self):
        try:
            self.conexao.rollback()
            return True
        except Error as e:
            print(f"Erro ao reverter transação: {e}")
            return False