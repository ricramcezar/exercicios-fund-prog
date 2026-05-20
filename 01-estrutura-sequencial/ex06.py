'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.
'''

# 1. Entrada de dados
salario_fixo = float(input("Digite o salário fixo do funcionário: R$ "))
valor_vendas = float(input("Digite o valor total de vendas: R$ "))

# 2. Processamento (Cálculos)
# 4% é o mesmo que 4 dividido por 100, ou seja, 0.04
comissao = valor_vendas * 0.04 
salario_final = salario_fixo + comissao

# 3. Saída de dados
print("\n--- Resumo do Salário ---")
print(f"Comissão recebida: R$ {comissao:.2f}")
print(f"Salário final a receber: R$ {salario_final:.2f}")