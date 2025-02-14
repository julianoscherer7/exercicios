CREATE DATABASE gestao_pessoal;

USE gestao_pessoal;

CREATE TABLE Funcionarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    cargo VARCHAR(50),
    departamento VARCHAR(50),
    email VARCHAR(100),
    data_contratacao DATE,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE Contratos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    funcionario_id INT,
    tipo_contrato ENUM('CLT', 'PJ', 'Estágio'),
    salario DECIMAL(10,2),
    data_inicio DATE,
    data_fim DATE,
    multa_rescisoria DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id)
);

CREATE TABLE Folha_Pagamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    funcionario_id INT,
    mes_ano DATE,
    horas_trabalhadas INT,
    valor_pago DECIMAL(10,2),
    descontos DECIMAL(10,2) DEFAULT 0,
    beneficios DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id)
);

CREATE TABLE Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario VARCHAR(50) UNIQUE,
    senha VARCHAR(100),
    perfil ENUM('admin', 'rh', 'financeiro')
);