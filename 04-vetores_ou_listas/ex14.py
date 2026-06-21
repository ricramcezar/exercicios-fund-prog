'''
Faça um programa que receba o nome e duas notas de seis alunos e mostre o relatório a seguir. 
Relatório de notas:

ALUNO       1a PROVA    2a PROVA    MÉDIA   SITUAÇÃO
Carlos      8,0         9,0         8,5     Aprovado
Pedro       4,0         5,0         4,5     Reprovado

-> média da classe = ?
-> percentual de alunos aprovados = ?%
-> percentual de alunos de exame = ?%
-> percentual de alunos reprovados = ?%
'''

lista_alunos = []
nota1 = []
nota2 = []
media_aluno = []

for i in range(6):
    nome_aluno = input("Digite o nome do aluno: ")
    lista_alunos.append(nome_aluno)
    nota_prova1 = float(input("Digite a nota da 1ª prova: "))
    nota1.append(nota_prova1)
    nota_prova2 = float(input("Digite a nota da 2ª prova: "))
    nota2.append(nota_prova2)
    media = (nota_prova1 + nota_prova2) / 2

for i in range(len(lista_alunos)):
    if media_aluno[i] >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"