'''
Uma empresa decide aplicar descontos nos seus preços usando a tabela a seguir. Faça um programa que receba o preço atual de um produto e seu código, calcule e mostre o valor do desconto e o novo preço.

PREÇO ATUAL             % DE DESCONTO
Até R$30                Sem desconto
Entre R$30 e R$100      10%
Acima de R$100          15%
'''

import sys

codigo = input("Digite o código do produto: ")
preco_atual = float(input("Digite o preço atual do produto: R$"))

if preco_atual <= 0.0:
	print("Erro: Digite um preço válido (maior que zero):")
	sys.exit()

if preco_atual <= 30:
	percentual_desconto = 0
elif preco_atual <= 100:
	percentual_desconto = 0.1
else:
	percentual_desconto = 0.15

valor_desconto = preco_atual * percentual_desconto
novo_preco = preco_atual - valor_desconto

print(f"\n--- Resumo do Produto: {codigo} ---")
print(f"Preço Original: R$ {preco_atual:>8.2f}")
print(f"Desconto ({int(percentual_desconto*100)}%): R$ {valor_desconto:>8.2f}")
print(f"Preço Final:    R$ {novo_preco:>8.2f}")
print("-" * 30)