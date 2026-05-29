'''
Faça um programa que receba cinco números e mostre a saída a seguir:
Digite o 1º número 5
Digite o 2º número 3
Digite o 3º número 2
Digite o 4º número 0
Digite o 5º número 2
Os números digitados foram: 5 + 3 + 2 + 0 + 2 = 12
'''

lista_numeros = []
soma_total = 0

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)
    soma_total += numero

expressao = " + ".join(map(str, lista_numeros))

print(f"Os números digitados foram: {expressao} = {soma_total}")