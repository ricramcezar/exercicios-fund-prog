'''
Faça um programa que receba a idade e a altura de várias pessoas, calcule e mostre a média das alturas daquelas com mais de 50 anos. Para encerrar a entrada de dados, digite idade menor ou igual a zero.
'''

quantidade = 0
soma_alturas = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade <= 0:
        break
    
    altura = float(input("Digite a altura em cm: "))
    if idade > 50:
        soma_alturas += altura
        quantidade += 1

if quantidade > 0:
    media = soma_alturas / quantidade
    print(f"A média das alturas das pessoas com mais de 50 anos é {media:.1f} cm.")
else:
    print("Não há pessoas com mais de 50 anos.")