'''
Faça um programa que receba a idade de oito pessoas, calcule e mostre:
a) a quantidade de pessoas em cada faixa etária;
b) a porcentagem de pessoas na primeira faixa etária com relação ao total de pessoas.
c) a porcentagem de pessoas na última faixa etária com relação ao total de pessoas.

FAIXA ETÁRIA    IDADE
1ª              Até 15 anos
2ª              De 16 a 30 anos
3ª              De 31 a 45 anos
4ª              De 46 a 60 anos
5ª              Acima de 60 anos
'''

idade = 0
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for i in range(8):
    idade = int(input("Digite a idade: "))
    if idade <= 15:
        faixa1 += 1
    elif idade <= 30:
        faixa2 += 1
    elif idade <= 45:
        faixa3 += 1
    elif idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

print(f"Quantidade de pessoas em cada faixa etária:\n"
      "--------------------------------------------\n"
      f"1ª: {faixa1} | 2ª: {faixa2} | 3ª: {faixa3} | 4ª: {faixa4} | 5ª: {faixa5}\n"
      f"Porcentagem da 1ª faixa: {((faixa1 / 8) * 100):.2f}%\n"
      f"Porcentagem da 5ª faixa: {((faixa5 / 8) * 100):.2f}%\n"
      "--------------------------------------------\n")