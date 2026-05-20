'''
Faça um programa que receba a idade de uma pessoa e mostre a mensagem de maioridade ou não.
'''

import sys

try:
    # Tenta converter a entrada para inteiro
    idade = int(input("Qual a sua idade? "))
except ValueError: # Caso o usuário digite letras ou o número por extenso
    print("Erro: Por favor, digite apenas números inteiros.")
    sys.exit()
		
if idade < 0:
	print("Erro: Digite uma idade válida.")
	sys.exit()

if idade >= 18:
	print("Você é maior de idade.")
else:
	print("Você é menor de idade.")