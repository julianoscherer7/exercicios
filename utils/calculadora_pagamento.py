class CalculadoraPagamento:
    def calcular_salario(self, contrato, horas):
        return contrato.salario * horas

    def calcular_liquido(self, bruto, descontos, beneficios):
        return bruto - descontos + beneficios