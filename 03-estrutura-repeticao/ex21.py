'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

1, 2, 3, 4  | Votos para os respectivos candidatos
5           | Voto nulo
6           | Voto em branco

Faça um programa que calcule e mostre:
-> o total de votos para cada candidato;
-> o total de votos nulos;
-> o total de votos em branco;
-> a porcentagem de votos nulos sobre o total de votos; e
-> a porcentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos, tem-se o valor zero e, para códigos inválidos, o programa deverá mostrar uma mensagem.
'''

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_candidato_4 = 0
votos_nulos = 0
votos_em_branco = 0

while True:
    print("\nDigite seu voto:\n"
          "\nCandidato 1 - digite [1]\n"
          "Candidato 2 - digite [2]\n"
          "Candidato 3 - digite [3]\n"
          "Candidato 4 - digite [4]\n")
    print("Voto nulo - digite [5]\n"
          "Voto em branco - digite [6]\n"
          "\nSair - digite [0]\n")
    
    try:
        voto = int(input("Digite seu voto ou [0] para sair: "))
    except ValueError:
        print('-' * 35)
        print("Código inválido. Digite apenas números.")
        print('-' * 35)
        continue

    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        votos_candidato_3 += 1
    elif voto == 4:
        votos_candidato_4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    elif voto == 0:
        break
    else:
        print('-' * 35)
        print("Código inválido. Tente novamente")
        print('-' * 35)
        continue

total_votos = votos_candidato_1 + votos_candidato_2 + votos_candidato_3 + votos_candidato_4 + votos_nulos + votos_em_branco

if total_votos > 0:
    porcentagem_nulos = (votos_nulos / total_votos) * 100
    porcentagem_em_branco = (votos_em_branco / total_votos) * 100
    print("------ TOTAL DE VOTOS ------")
    print(f"Candidato 1: {votos_candidato_1} votos\n"
          f"Candidato 2: {votos_candidato_2} votos\n"
          f"Candidato 3: {votos_candidato_3} votos\n"
          f"Candidato 4: {votos_candidato_4} votos\n")
    print(f"Votos nulos: {votos_nulos} votos\n"
          f"Votos em branco: {votos_em_branco} votos\n")
    print(f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%\n"
          f"Porcentagem de votos em branco: {porcentagem_em_branco:.2f}%\n")
else:
    print("Não houve votos registrados.")