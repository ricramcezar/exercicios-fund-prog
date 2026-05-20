'''
Faça um programa que receba:
-> o código do produto comprado; e
-> a quantidade comprada do produto.

Calcule e mostre:
-> o preço unitário do produto comprado, seguindo a Tabela I;
-> o preço total da nota;
-> o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e
-> o preço final da nota depois do desconto.

TABELA I                        TABELA II
CÓDIGO      PREÇO               PREÇO TOTAL DA NOTA         % DE DESCONTO
1 a 10      R$ 10               Até R$ 250                  5%
11 a 20     R$ 15               Entre R$ 250 e R$ 500       10%
21 a 30     R$ 20               Acima de R$ 500             15%
31 a 40     R$ 30
'''

import sys

try:
    codigo_produto = int(input("Digite o código do produto [1 a 40]: "))
    qtde_produto = int(input("Digite a quantidade comprada: "))
except ValueError:
    print("Erro: Digite apenas números válidos para código e quantidade.")
    sys.exit()

if codigo_produto <= 0 or codigo_produto > 40 or qtde_produto <= 0:
    print("Erro: Digite apenas de 1 a 40 para o código e números maiores que zero para quantidade.")
    sys.exit()

if codigo_produto in range(1, 11):
    preco_produto = 10
elif codigo_produto in range(11, 21):
    preco_produto = 15
elif codigo_produto in range(21, 31):
    preco_produto = 20
else:
    preco_produto = 30

total_nota = preco_produto * qtde_produto

if total_nota <= 250:
    percentual = 5
elif total_nota <= 500:
    percentual = 10
else:
    percentual = 15

desconto = total_nota * (percentual / 100)
preco_final = total_nota - desconto

print("\n--- DADOS DE COMPRA ---")
print(f"Preço unitário: R$ {preco_produto:.2f}\n"
      f"Preço Total da Nota: R$ {total_nota:.2f}\n"
      f"Valor do Desconto ({percentual}%): R$ {desconto:.2f}\n"
      f"Preço Final: R$ {preco_final:.2f}\n")