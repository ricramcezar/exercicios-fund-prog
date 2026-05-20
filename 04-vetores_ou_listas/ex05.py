'''
Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos que cursam Lógica em uma lista, quinze alunos. Coloque os números das matrículas dos alunos que cursam Linguagem de Programação em outra lista, dez alunos. Mostre o número das matrículas que aparecem nas duas listas.
'''

alunos_logica = []

for i in range(15):
    matricula_logica = input("Digite o número da matrícula para Lógica: ")
    alunos_logica.append(matricula_logica)

alunos_linguagem = []

for i in range(10):
    matricula_linguagem = input("Digite o número da matrícula para Linguagem de Programação: ")
    alunos_linguagem.append(matricula_linguagem)

matriculas_comuns = []

for matricula in alunos_logica:
    if matricula in alunos_linguagem:
        matriculas_comuns.append(matricula)


print("\nMatrícula(s) cursando as duas disciplinas:", ", ".join(matriculas_comuns))