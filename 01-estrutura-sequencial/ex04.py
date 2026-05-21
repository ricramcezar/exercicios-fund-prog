'''
Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso1 = 2
peso2 = 3
media_final = ((nota1 * peso1) + (nota2 * peso2)) / (peso1 + peso2)

print(f"A média ponderada das notas é: {media_final:.2f}.")
