'''
Foi feita uma pesquisa sobre a audiência de canal de TV em várias casas de uma cidade, em determinado dia. Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo àquele canal. Se a televisão estivesse desligada, nada era anotado, ou seja, essa casa não entrava na pesquisa. Faça um programa que:

-> leia um número indeterminado de dados (número do canal e número de pessoas que estavam assistindo); e
-> calcule e mostre a porcentagem de audiência de cada canal.

Para encerrar a entrada de dados, digite o número do canal ZERO.
'''

audiencia = {
    4: 0,
    5: 0,
    7: 0,
    12: 0,
}

total_geral = 0

while True:
    canal = int(input("Digite o número do canal (4, 5, 7 ou 12) ou 0 para sair: "))
    if canal == 0:
        break

    if canal in audiencia:
        pessoas = int(input("Digite a quantidade de pessoas assistindo ao canal: "))
        audiencia[canal] += pessoas
        total_geral += pessoas
    else:
        print("Canal inválido! Por favor, digite 4, 5, 7 ou 12.")

if total_geral > 0:
    print("\n--- Resultado da Audiência ---")
    for canal, pessoas in audiencia.items():
        porcentagem = (pessoas / total_geral) * 100
        print(f"Canal {canal}: {porcentagem:.2f}% de audiência.")
else:
    print("Nenhum dado de audiência foi registrado.")
