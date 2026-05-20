'''
Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e sua opinião em relação ao filme: ótimo — 3; bom — 2; regular — 1. Faça um programa que receba a idade e a opinião de quinze espectadores, calcule e mostre:

-> a média das idades das pessoas que responderam ótimo;
-> a quantidade de pessoas que responderam regular; e
-> a percentagem de pessoas que responderam bom, entre todos os espectadores analisados.
'''

TOTAL_ESPECTADORES = 15

idade_otimo = []
qtd_regular = 0
qtd_bom = 0

for i in range(TOTAL_ESPECTADORES):
    idade = int(input("Qual a sua idade?: "))
    opiniao = int(input("Qual a sua opinião sobre o filme?\n"
                        "Responda [3] - Ótimo, [2] - bom, ou [1] - regular: "))
    if opiniao == 3:
        idade_otimo.append(idade)
    elif opiniao == 1:
        qtd_regular += 1
    elif opiniao == 2:
        qtd_bom += 1

if idade_otimo:
    media_otimo = sum(idade_otimo) / len(idade_otimo)
    print(f"Média das idades das pessoas que responderam 'ótimo': {media_otimo:.2f}")
else:
    print("Nenhuma pessoa respondeu 'ótimo'.")

    print(f"Quantidade de pessoas que responderam 'regular': {qtd_regular}")

if qtd_bom > 0:
    porcentagem_bom = (qtd_bom / TOTAL_ESPECTADORES) * 100
    print(f"Porcentagem de pessoas que responderam 'bom': {porcentagem_bom:.2f}%")
