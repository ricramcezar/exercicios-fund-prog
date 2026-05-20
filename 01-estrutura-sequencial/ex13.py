'''
Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.
  Exemplo:
  Digite um número: 5
    5 * 0 = 0             5 * 6 = 30
    5 * 1 = 5             5 * 7 = 35
    5 * 2 = 10            5 * 8 = 40
    5 * 3 = 15            5 * 9 = 45
    5 * 4 = 20            5 * 10 = 50
    5 * 5 = 25
'''

# 1. Entrada de dados
numero = int(input("Digite um número de 1 a 10: "))

print() # Pula uma linha

# 2. Processamento e Saída sequencial
print(f"{numero} x 0 = {numero * 0}")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")