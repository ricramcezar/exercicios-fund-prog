'''
Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

TABELA DAS GRATIFICAÇÕES

SALÁRIO               GRATIFICAÇÃO
Até R$350             R$100
> R$350 e < R$600     R$75
>= R$600 e <= R$900   R$50
Acima de R$900        R$35
'''

import sys

salario_bruto = float(input("Digite o valor do salário bruto: R$"))

if salario_bruto <= 0:
  print("Erro: Digite um valor válido (maior que zero).")
  sys.exit()

if salario_bruto <= 350:
  gratificacao = 100
elif salario_bruto < 600:
  gratificacao = 75
elif salario_bruto <= 900:
  gratificacao = 50
else:
  gratificacao = 35

imposto = salario_bruto * 0.07
total_receber = salario_bruto + gratificacao - imposto

print(f"\nSalário bruto: R${salario_bruto:.2f}"
      f"\nGratificação: R${gratificacao:.2f}"
      f"\nImposto a deduzir: R${imposto:.2f}"
      f"\nTotal a receber: R${total_receber:.2f}\n")