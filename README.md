# 📊 Sistema de Registro de Alunos

Projeto desenvolvido para demonstrar conhecimento e evolução em **Python**, **MySQL** e **Excel**, 
conectando as três ferramentas em um sistema completo de cadastro e análise de dados escolares.

## 🎯 Objetivo

Desenvolver um sistema que cadastra nomes e notas de alunos, armazena os dados em um banco 
MySQL, gera um relatório de aprovação/reprovação no terminal e exporta automaticamente 
uma tabela Excel para análise dos dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **MySQL**
- **Excel** (via biblioteca `openpyxl`)
- **Bibliotecas:** `mysql-connector-python`, `openpyxl`, `python-dotenv`

## 📁 Estrutura do Projeto

### 🐍 Programa Python
Responsável por coletar os dados dos alunos via terminal, calcular médias, 
verificar aprovação e exibir o relatório final.

### 🗄️ Armazenamento MySQL
Armazena os dados em duas tabelas relacionadas:
- `aluno` — registra nome e quantidade de semestres
- `nota` — registra cada nota vinculada ao respectivo aluno via chave estrangeira

### 📄 Exportação Excel
Gera automaticamente uma planilha com cabeçalho e todos os registros 
inseridos, utilizando JOIN entre as tabelas para consolidar os dados.

## 🔒 Segurança
As credenciais do banco de dados são protegidas com `.env` e `python-dotenv`, 
não sendo expostas no código-fonte.

## 📚 Aprendizados

- Conexão entre Python e MySQL com `mysql-connector-python`
- Normalização de banco de dados com chave estrangeira
- Exportação de dados para Excel com `openpyxl`
- Proteção de credenciais com `python-dotenv`
- Uso de laços de repetição, funções e dicionários em Python
- Consultas SQL com `JOIN` entre tabelas relacionadas

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3 instalado
- MySQL instalado
- VS Code ou outro editor que execute Python

### 1. Clone o repositório
```bash
git clone https://github.com/JulianoSR/Sistema_registro_Alunos.git
```

### 2. Instale as bibliotecas
```bash
pip install mysql-connector-python
pip install openpyxl
pip install python-dotenv
```

### 3. Configure o banco de dados
No MySQL, execute:
```sql
CREATE DATABASE registro_aluno;
USE registro_aluno;

CREATE TABLE aluno (
    id_aluno INT PRIMARY KEY AUTO_INCREMENT,
    nome_aluno VARCHAR(100) NOT NULL,
    qtd_semestre INT NOT NULL
);

CREATE TABLE nota (
    id_nota INT PRIMARY KEY AUTO_INCREMENT,
    id_aluno INT,
    FOREIGN KEY(id_aluno) REFERENCES aluno(id_aluno),
    semestre INT NOT NULL,
    nota FLOAT NOT NULL
);
```

### 4. Configure o arquivo .env
Crie um arquivo `.env` na pasta do projeto com suas credenciais:

### 5. Execute o programa
```bash
python ProjetoPortfólio.py
```
