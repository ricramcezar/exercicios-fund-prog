'''
Faça um programa que receba o preço, a categoria (1 - limpeza; 2 - alimentação; ou 3 - vestuário) e a situação (R - produtos que necessitam de refrigeração; e N - produtos que não necessitam de refrigeração).

Calcule e mostre:

-> O valor do aumento, usando as regras que se seguem.

PREÇO       CATEGORIA       PERCENTUAL DE AUMENTO
<= 25       1               5%
            2               8%
            3               10%
> 25        1               12%
            2               15%
            3               18%

-> O valor do imposto, usando as regras a seguir:

O produto que preencher pelo menos um dos seguintes requisitos pagará imposto equivalente a 5% do preço; caso contrário, pagará 8%. Os requisitos são:

Categoria: 2
Situação: R

-> O novo preço, ou seja, o preço mais aumento menos imposto.
-> A classificação, usando as regras a seguir:

NOVO PREÇO              CLASSIFICAÇÃO
<= R$ 50                Barato
Entre R$ 50 e R$ 120    Normal
>= R$ 120               Caro
'''

import sys

try:
    preco = float(input("Digite o preço do produto. Use ponto [.] para centavos (ex.: 13.45): R$ "))
    categoria = int(input("[1] - Limpeza | [2] - alimentação | [3] - vestuário\nDigite a categoria desejada [1, 2 ou 3]: "))
    situacao = input("[R] - produtos que necessitam de refrigeração\n[N] - produtos que não necessitam de refrigeração\nDigite [R] ou [N]: ").strip().upper()
except ValueError:
    print("\nErro: Entrada inválida.")
    print("Certifique-se de usar números para preço/categoria e ponto para decimais.")
    sys.exit()
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
    sys.exit()

if categoria not in [1, 2, 3] or situacao not in ["R", "N"]:
    print("\nErro: Categoria ou Situação Inválida.")
    print("Use [1, 2 ou 3] para categoria e [R ou N] para situação.")
    sys.exit()

if preco <= 0:
    print("\nErro: O preço deve ser maior que zero.")
    sys.exit()

if preco <= 25:
    if categoria == 1:
        percentual = 5
    elif categoria == 2:
        percentual = 8
    else:
        percentual = 10
else:
    if categoria == 1:
        percentual = 12
    elif categoria == 2:
        percentual = 15
    else:
        percentual = 18

valor_aumento = preco * (percentual / 100)

imposto1 = 5
imposto2 = 8

if categoria == 2 or situacao == "R":
    imposto_final = preco * (imposto1 / 100)
else:
    imposto_final = preco * (imposto2 / 100)

novo_preco = preco + valor_aumento - imposto_final

if novo_preco <= 50:
    classificacao = "Barato"
elif novo_preco < 120:
    classificacao = "Normal"
else:
    classificacao = "Caro"

print("\n" + "="*30)
print(f"VALOR DO AUMENTO: R$ {valor_aumento:.2f}")
print(f"VALOR DO IMPOSTO: R$ {imposto_final:.2f}")
print(f"NOVO PREÇO:       R$ {novo_preco:.2f}")
print(f"CLASSIFICAÇÃO:    {classificacao}")
print("="*30 + "\n")