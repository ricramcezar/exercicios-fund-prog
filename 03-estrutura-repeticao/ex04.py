'''
Faça um programa que receba um número, calcule e mostre a tabuada desse número.
'''

numero = int(input("Digite um número inteiro positivo: "))
multiplicador = -1

while multiplicador < 10:
    multiplicador += 1
    produto = numero * multiplicador
    print(f"{numero} x {multiplicador} = {produto}")
