'''
Faça um programa que preencha uma lista com seis elementos numéricos inteiros. Calcule e mostre:

-> todos os números pares;
-> a quantidade de números pares;
-> todos os números ímpares;
-> a quantidade de números ímpares.
'''

lista_numeros = []

for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

lista_pares = []
lista_impares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

qtd_pares = len(lista_pares)
qtd_impares = len(lista_impares)

print(f"\nNúmeros pares: {lista_pares}")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Números ímpares: {lista_impares}")
print(f"Quantidade de números ímpares: {qtd_impares}\n")