'''
Faça um programa que receba o salário de um funcionário e, usando a tabela a seguir, calcule e mostre o novo salário.

FAIXA SALARIAL              % DE AUMENTO
Até R$300                   50%
> R$300 e <= R$500          40%
> R$500 e <= R$700          30%
> R$700 e <= R$800          20%
> R$800 e <= R$1000         10%
Acima de R$1000             5%
'''

import sys

salario = float(input("Digite o valor do salário: R$"))

if salario <= 0:
  print("Erro: Digite um salário válido (maior que zero).")
  sys.exit()

if salario <= 300:
  aumento = salario * 0.5
elif salario <= 500:
  aumento = salario * 0.4
elif salario <= 700:
  aumento = salario * 0.3
elif salario <= 800:
  aumento = salario * 0.2
elif salario <= 1000:
  aumento = salario * 0.1
else:
  aumento = salario * 0.05

novo_salario = salario + aumento

print(f"\nSalário anterior: R${salario:.2f}"
      f"\nNovo salário: R${novo_salario:.2f}\n")