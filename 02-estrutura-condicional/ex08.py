'''
Faça um programa para calcular e mostrar o salário reajustado de um funcionário. O percentual de aumento encontra-se na tabela a seguir.

SALÁRIO               PERCENTUAL DE AUMENTO
Até R$ 300,00         35%
Acima de R$ 300,00    15%
'''

print("=" * 50)
salario = float(input("Digite o salário do funcionário: R$"))

if salario <= 0:
  print("Erro: Digite um salário válido (maior que zero).")

elif salario <= 300:
  aumento = salario * 0.35
  salario_reajustado = salario + aumento
  print(f"\nVocê recebe R${salario:.2f}, com 35% de aumento, receberá um total de R${salario_reajustado:.2f}.")
else:
  aumento = salario * 0.15
  salario_reajustado = salario + aumento
  print(f"\nVocê recebe R${salario:.2f}, com 15% de aumento, receberá um total de R${salario_reajustado:.2f}.")

print("=" * 50)