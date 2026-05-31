import mysql.connector
import openpyxl

import mysql.connector
import openpyxl
from dotenv import load_dotenv
import os

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE")
)

cursor = conexao.cursor()
estudantes = []

def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media

def verificar_aprovacao(media, media_minima=7.0):
    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'

def gerar_relatorio(alunos):
    print("========== RELATÓRIO ==========")
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = verificar_aprovacao(media)
        print(f"Nome: {aluno['nome']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("-------------------------------")

inicio_programa = input("Deseja cadastrar um aluno? S/N ")

while inicio_programa == "S":
    nome_aluno = input("Qual o nome do Aluno? ")
    notas_aluno = []
    semestre_escolar = 1
    while semestre_escolar <= 4:
        notas_aluno.append(float(input("Qual a nota do aluno? ")))
        semestre_escolar = semestre_escolar + 1
    estudante = {"nome": nome_aluno, "notas": notas_aluno}
    estudantes.append(estudante)
    cursor.execute(
        "INSERT INTO aluno (nome_aluno, qtd_semestre) VALUES (%s, %s)",
        (nome_aluno, len(notas_aluno))
    )
    print("INSERT aluno executado!")
    id_aluno = cursor.lastrowid
    for semestre, nota in enumerate(notas_aluno, 1):
        cursor.execute(
            "INSERT INTO nota (id_aluno, semestre, nota) VALUES (%s, %s, %s)",
            (id_aluno, semestre, nota)
        )
    inicio_programa = input("Deseja cadastrar mais um aluno? S/N ")

conexao.commit()
planilha = openpyxl.Workbook()
aba = planilha.active
cursor.execute("select aluno.id_aluno, id_nota, nome_aluno, semestre, nota from aluno join nota on aluno.id_aluno = nota.id_aluno")
resultados = cursor.fetchall()
aba.append(["id_aluno", "id_nota", "nome", "semestre", "nota"])
for linha in resultados:
    aba.append(linha)
planilha.save("relatorio_alunos.xlsx")
gerar_relatorio(estudantes)
conexao.close()