'''
Uma agência bancária possui dois tipos de investimentos, conforme o quadro a seguir. Faça um programa que receba o tipo de investimento e seu valor, calcule e mostre o valor corrigido após um mês de investimento, de acordo com o tipo de investimento.

TIPO    DESCRIÇÃO             RENDIMENTO MENSAL
1       Poupança              3%
2       Fundos de renda fixa  4%
'''

import sys

tipo_investimento = int(input("Escolha [1] para Poupança e [2] para Fundos de renda fixa: "))
valor_investimento = float(input("Digite o valor do investimento: R$"))

if tipo_investimento not in [1, 2]:
  print("Erro: Tipo de Investimento Inválido")
  sys.exit()

if valor_investimento <= 0:
  print("Erro: Digite um valor válido (maior que zero).")
  sys.exit()

if tipo_investimento == 1:
  nome_investimento = "Poupança"
  rendimento = valor_investimento * 0.03
else:
  nome_investimento = "Fundos de renda fixa"
  rendimento = valor_investimento * 0.04

valor_corrigido = valor_investimento + rendimento

print(f"\n--- Resumo da Operação ---"
      f"\nTipo de Investimento: {nome_investimento}"
      f"\nValor investido: R${valor_investimento:.2f}"
      f"\nValor corrigido (um mês): R${valor_corrigido:.2f}\n")