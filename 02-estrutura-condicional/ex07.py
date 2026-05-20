'''
Uma empresa decide dar um aumento de 30% aos funcionários com salários inferiores a R$ 500,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso ele não tenha direito ao aumento.
'''

salario = float(input("Digite o salário do funcionário: R$"))

if salario < 500:
  aumento = salario * 0.3
  salario_reajustado = salario + aumento

  print(f"\nVocê recebe R${salario:.2f}, então você recebe R${aumento:.2f} de aumento.\n"
        f"Seu salário reajustado é R${salario_reajustado:.2f}.\n")
else:
  print(f"\nVocê recebe R${salario:.2f} e não tem direito a aumento.\n")