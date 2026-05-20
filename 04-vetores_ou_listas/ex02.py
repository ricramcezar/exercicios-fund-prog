'''
Faça um programa que preencha uma lista com sete números inteiros, calcule e mostre:
-> os números múltiplos de 2;
-> os números múltiplos de 3;
-> os números múltiplos de 2 e de 3.
'''

lista_numeros = []

for _ in range(7):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

multiplos2 = []
multiplos3 = []
multiplos2_3 = []

for numero in lista_numeros:
    if numero % 2 == 0:
        multiplos2.append(numero)
    if numero % 3 == 0:
        multiplos3.append(numero)
    if numero % 2 == 0 and numero % 3 == 0:
        multiplos2_3.append(numero)

if multiplos2:
    print(f"\nMúltiplos de 2: {multiplos2}")
else: 
    print("Não há números que sejam múltiplos de 2.")

if multiplos3:
    print(f"Múltiplos de 3: {multiplos3}")
else:
    print("Não há números que sejam múltiplos de 3.")

if multiplos2_3:
    print(f"Múltiplos de 2 e 3: {multiplos2_3}\n")
else:
    print("Não há números que sejam ao mesmo tempo múltiplos de 2 e 3.\n")