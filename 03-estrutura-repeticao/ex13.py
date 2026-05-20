'''
Faça um programa que receba a idade e o peso de quinze pessoas, e que calcule e mostre as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e de 31 anos para cima.
'''

TOTAL_PESSOAS = 15
faixa1 = []
faixa2 = []
faixa3 = []
faixa4 = []

for i in range(TOTAL_PESSOAS):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (use ponto [.] para gramas - ex. 76.5): "))
    if idade <= 10:
        faixa1.append(peso)
    elif idade <= 20:
        faixa2.append(peso)
    elif idade <= 30:
        faixa3.append(peso)
    else:
        faixa4.append(peso)

if len(faixa1) > 0:
    media_faixa1 = sum(faixa1) / len(faixa1)
    print(f"Média de peso (1 a 10 anos): {media_faixa1:.2f} kg")
else:
    print("Nenhuma pessoa registrada nesta faixa.")

if len(faixa2) > 0:
    media_faixa2 = sum(faixa2) / len(faixa2)
    print(f"Média de peso (11 a 20 anos): {media_faixa2:.2f} kg")
else:
    print("Nenhuma pessoa registrada nesta faixa.")

if len(faixa3) > 0:
    media_faixa3 = sum(faixa3) / len(faixa3)
    print(f"Média de peso (21 a 30 anos): {media_faixa3:.2f} kg")
else:
    print("Nenhuma pessoa registrada nesta faixa.")

if len(faixa4) > 0:
    media_faixa4 = sum(faixa4) / len(faixa4)
    print(f"Média de peso (acima de 31 anos): {media_faixa4:.2f} kg")
else:
    print("Nenhuma pessoa registrada nesta faixa.")