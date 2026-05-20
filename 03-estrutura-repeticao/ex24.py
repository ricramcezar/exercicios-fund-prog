'''
Faça um programa que receba um conjunto de valores inteiros e positivos, calcule e mostre o maior e o menor valor do conjunto. Considere que:

-> para encerrar a entrada de dados, deve ser digitado o valor zero;
-> para valores negativos, deve ser enviada uma mensagem;
-> os valores negativos ou iguais a zero não entrarão nos cálculos.
'''

lista_valores = []

while True:
    numero = int(input("Digite um valor inteiro e positivo: "))
    if numero == 0:
        break
    elif numero < 0:
        print("Valor inválido. Digite apenas valores positivos.")
    else:
        lista_valores.append(numero)

if lista_valores:
    print(f"\nMaior valor registrado: {max(lista_valores)}\n"
          f"Menor valor registrado: {min(lista_valores)}\n")
else:
    print("Nenhum valor positivo foi informado.")