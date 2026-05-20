'''
Faça um programa que receba o total das vendas de cada vendedor de uma loja e armazene-as em uma lista. Receba também o percentual de comissão a que cada vendedor tem direito e armazene-os em outra lista. Receba os nomes desses vendedores e armazene-os em uma terceira lista. Existem apenas dez vendedores na loja. Calcule e mostre:

-> um relatório com os nomes dos vendedores e os valores a receber referentes à comissão;
-> o total das vendas de todos os vendedores;
-> o maior valor a receber e o nome de quem o receberá;
-> o menor valor a receber e o nome de quem o receberá.
'''

total_vendas = []
percentual_comissao = []
vendedores = []

for i in range(10):
    vendedor = input("Digite o nome do vendedor: ")
    vendedores.append(vendedor)
    vendas = float(input("Digite o total das vendas do vendedor: R$ "))
    total_vendas.append(vendas)
    comissao = float(input("Digite o percentual de comissão para o vendedor (Não digite o símbolo %): "))
    percentual_comissao.append(comissao)

valor_comissao = []

for i in range(len(vendedores)):
    total_comissao = total_vendas[i] * percentual_comissao[i] / 100
    valor_comissao.append(total_comissao)

total_vendas_geral = sum(total_vendas)

maior_valor = max(valor_comissao)
pos_maior_valor = valor_comissao.index(maior_valor)
nome_vendedor_maior = vendedores[pos_maior_valor]

menor_valor = min(valor_comissao)
pos_menor_valor = valor_comissao.index(menor_valor)
nome_vendedor_menor = vendedores[pos_menor_valor]

print("\n### RELATÓRIO DE COMISSÕES ###\n")

for i in range(len(vendedores)):
    print(f"Nome do vendedor: {vendedores[i]}")
    print(f"Valor da comissão: R$ {valor_comissao[i]:.2f}\n")

print("### RESUMO FINAL ###\n")

print(f"Total das vendas: R$ {total_vendas_geral:.2f}")
print(f"Maior valor a receber: R$ {maior_valor:.2f}")
print(f"Vendedor com maior comissão: {nome_vendedor_maior}")
print(f"Menor valor a receber: R$ {menor_valor:.2f}")
print(f"Vendedor com menor comissão: {nome_vendedor_menor}\n")