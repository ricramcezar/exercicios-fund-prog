'''
Faça um programa que receba dez números inteiros e armazene-os em uma lista. Calcule e mostre duas listas resultantes: o primeiro com os números pares e o segundo, com os números ímpares.
'''

numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")