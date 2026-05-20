'''
Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários mínimos que esse funcionário ganha.
'''

# Dados

salario_minimo = float(input("Digite o salário mínimo atual: R$"))
salario_funcionario = float(input("Digite o salário do funcionário: R$"))

# Cálculo

quantidade_salarios = (salario_funcionario / salario_minimo)
print(f"O funcionário ganha {quantidade_salarios:.2f} salários mínimos.")