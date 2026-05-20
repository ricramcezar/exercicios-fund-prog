'''
Faça um programa que receba a idade, a altura e o peso de cinco pessoas, calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos;
b) a média das alturas das pessoas com idade entre 10 e 20 anos;
c) a porcentagem de pessoas com peso inferior a 40 kg entre todas as pessoas analisadas.
'''

TOTAL_PESSOAS = 5
idade = 0
altura = 0
peso = 0
cont_50 = 0
soma_alturas = 0
cont_altura = 0
cont_peso = 0
porcentagem_peso = 0

for pessoa in range(TOTAL_PESSOAS):
    idade = int(input("Digite a idade: "))
    if idade > 50:
        cont_50 += 1
    altura = int(input("Digite a altura em cm (ex. 175 cm): "))
    if idade >= 10 and idade <= 20:
        soma_alturas += altura
        cont_altura += 1
    peso = float(input("Digite o peso - use ponto [.] para gramas (ex.: 82.5): "))
    if peso < 40:
        cont_peso += 1

porcentagem_peso = (cont_peso / TOTAL_PESSOAS) * 100

if cont_altura > 0:
    media_alturas = soma_alturas / cont_altura
else:
    media_alturas = 0

print(f"\n--- RELATÓRIO FINAL ---\n"
      f"Pessoas acima de 50 anos: {cont_50}\n"
      f"Média das alturas (entre 10 e 20 anos): {media_alturas} cm\n"
      f"% pessoas com peso inferior a 40kg: {porcentagem_peso:.2f}%\n")