'''
Faça um programa que receba o nome e a nota de oito alunos e mostre o relatório a seguir:
Digite o nome do 1o aluno: Carlos
Digite a nota do Carlos: 8
Digite o nome do 2o aluno: Pedro
Digite a nota do Pedro: 5
Relatórios de notas
Carlos 8.0
Pedro 5.0
..
..
..
Média da classe = ??
'''

lista_alunos = []
lista_notas = []

for i in range(8):
    nome_aluno = input(f"Digite o nome do {i + 1}º aluno: ")
    lista_alunos.append(nome_aluno)
    nota_aluno = float(input(f"Digite a nota do {nome_aluno}: "))
    lista_notas.append(nota_aluno)

print("Relatórios de notas")

for i in range(len(lista_alunos)):
    print(f"{lista_alunos[i]} {lista_notas[i]}")

media_classe = sum(lista_notas) / len(lista_notas)
print(f"Média da classe = {media_classe:.1f}")