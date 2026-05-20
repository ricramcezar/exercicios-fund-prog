'''
Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.

TABELA 1 - PERCENTUAL DE AUMENTO

PREÇO                   %
---------------------------
Até R$50                5
Entre R$50 e R$100      10
Acima de R$100          15

TABELA 2 - CLASSIFICAÇÕES

NOVO PREÇO                        CLASSIFICAÇÃO
------------------------------------------------
Até R$80                          Barato
Entre R$80 e R$120 (inclusive)    Normal
Entre R$120 e R$200 (inclusive)   Caro
Maior que R$200                   Muito caro
'''

import sys

valor_produto = float(input("Digite o valor do produto: R$"))

if valor_produto <= 0:
  print("Erro: Digite um valor válido (maior que zero).")
  sys.exit()

if valor_produto <= 50:
  aumento = valor_produto * 0.05
elif valor_produto <= 100:
  aumento = valor_produto * 0.10
else:
  aumento = valor_produto * 0.15

novo_valor = valor_produto + aumento

if novo_valor <= 80:
  classificacao = "Barato"
elif novo_valor <= 120:
  classificacao = "Normal"
elif novo_valor <= 200:
  classificacao = "Caro"
else:
  classificacao = "Muito caro"

print(f"\nPreço original: R${valor_produto:.2f}"
      f"\nNovo preço: R${novo_valor:.2f}"
      f"\nClassificação: {classificacao}\n")