'''
O preço ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a seguir. Faça um programa que receba o custo de fábrica de um carro e mostre o preço ao consumidor.

CUSTO DE FÁBRICA                % DO DISTRIBUIDOR               % DOS IMPOSTOS
Até R$12.000                     5                               isento
Entre R$12.000 e R$25.000        10                              15
Acima de R$25.000                15                              20
'''
import sys

custo_de_fabrica = float(input("Digite o valor do custo de fábrica: R$"))

if custo_de_fabrica <= 0:
  print("Erro: Digite um valor válido (maior que zero).")
  sys.exit()

if custo_de_fabrica <= 12000:
  porcentagem_distribuidor = custo_de_fabrica * 0.05
  impostos = 0
elif custo_de_fabrica <= 25000:
  porcentagem_distribuidor = custo_de_fabrica * 0.10
  impostos = custo_de_fabrica * 0.15
else:
  porcentagem_distribuidor = custo_de_fabrica * 0.15
  impostos = custo_de_fabrica * 0.20

preco_consumidor = custo_de_fabrica + porcentagem_distribuidor + impostos

print(f"\nCusto de fábrica: R${custo_de_fabrica:.2f}\n"
      f"Porcentagem do distribuidor: R${porcentagem_distribuidor:.2f}\n"
      f"Impostos: R${impostos:.2f}\n"
      f"Preço final ao consumidor: R${preco_consumidor:.2f}\n")
