'''
Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.

IDADE                                           PESO
                        Até 60      Entre 60 e 90 (inclusive)   Acima de 90
Menores que 20             9                       8                   7   
De 20 a 50                 6                       5                   4
Maiores que 50             3                       2                   1
'''

import sys

try:
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso (use ponto [.] para gramas): "))
except ValueError:
    print("Erro: Certifique-se de digitar números válidos para idade e peso.")
    sys.exit()

if idade <= 0 or peso <= 0:
    print("Erro: Digite um número válido (maior que zero).")
    sys.exit()

if idade < 20:
    if peso < 60:
        grupo_de_risco = 9
    elif peso <= 90:
        grupo_de_risco = 8
    else:
        grupo_de_risco = 7
elif idade <= 50:
    if peso < 60:
        grupo_de_risco = 6
    elif peso <= 90:
        grupo_de_risco = 5
    else:
        grupo_de_risco = 4
else:
    if peso < 60:
        grupo_de_risco = 3
    elif peso <= 90:
        grupo_de_risco = 2
    else: 
        grupo_de_risco = 1

print("--- Diagnóstico ---")
print(f"IDADE: {idade} anos")
print(f"PESO: {peso:.1f} kg")
print(f"GRUPO DE RISCO: {grupo_de_risco}\n")