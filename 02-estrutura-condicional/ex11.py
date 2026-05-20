'''
Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir, calcule e mostre o valor do aumento e o novo salário.

SALÁRIO                   PERCENTUAL DE AUMENTO
Até R$300                 15%
> R$300 e < R$600         10%
>= R$600 e <= R$900       5%
Acima de R$900            0%

'''

import sys

salario = float(input("Digite o valor do salário: R$"))

if salario <= 0:
  print("Erro: Digite um valor válido (maior que zero).")
  sys.exit()

if salario <= 300:
  aumento = salario * 0.15
elif salario < 600:
  aumento = salario * 0.10
elif salario <= 900:
  aumento = salario * 0.05
else:
  aumento = 0

novo_salario = salario + aumento
print(f"\nO funcionário recebe: R${salario:.2f}"
      f"\nValor do aumento: R${aumento:.2f}"
      f"\nNovo salário: R${novo_salario:.2f}\n")