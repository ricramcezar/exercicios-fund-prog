'''
Faça um programa que preencha uma lista com os nomes de sete alunos e carregue outra lista com a média final desses alunos. Calcule e mostre:

-> o nome do aluno com maior média (desconsiderar empates);
-> para cada aluno não aprovado, isto é, com média menor que 7, mostrar quanto esse aluno precisa tirar na prova de exame final para ser aprovado. Considerar que a média para aprovação no exame é 5.
'''

alunos = []
media_final = []

for i in range(7):
    aluno = input("Digite o nome: ")
    alunos.append(aluno)

    media = float(input("Digite a média final: "))
    media_final.append(media)

maior_media = max(media_final)
posicao = media_final.index(maior_media)
aluno_maior_media = alunos[posicao]

print(f"\nAluno com maior média: {aluno_maior_media}")
print(f"Maior média: {maior_media:.1f}")

print("\nAlunos em exame final:")

for i in range(len(alunos)):
    if media_final[i] < 7:
        nota_exame = 10 - media_final[i]
        print(f"{alunos[i]} precisa tirar {nota_exame:.1f} no exame final.")
        print()