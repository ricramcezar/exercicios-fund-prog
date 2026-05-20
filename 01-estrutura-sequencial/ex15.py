'''
João recebeu seu salário e precisa pagar duas contas atrasadas. Em razão do atraso, ele deverá pagar multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário de João.
'''

# Entrada de dados

salario_recebido = float(input("Digite o salário recebido por João: R$"))
valor_conta1 = float(input("Digite o valor original da primeira conta: R$"))
valor_conta2 = float(input("Digite o valor original da segunda conta: R$"))

# Cálculos

valor_final_conta1 = valor_conta1 + (valor_conta1 * 0.02)
valor_final_conta2 = valor_conta2 + (valor_conta2 * 0.02)
salario_restante = salario_recebido - valor_final_conta1 - valor_final_conta2

# Print

print(f"\nO funcionário recebeu R${salario_recebido:.2f}.")
print(f"\nA primeira conta tinha o valor original de R${valor_conta1:.2f}.\n"
      f"Com a multa, o valor da primeira conta ficou R${valor_final_conta1:.2f}")
print(f"\nA segunda conta tinha o valor original de R${valor_conta2:.2f}.\n"
      f"Com a multa, o valor da segunda conta ficou R${valor_final_conta2:.2f}.")
print(f"\nAo pagar as duas contas, o funcioário ficou com R${salario_restante:.2f}.")