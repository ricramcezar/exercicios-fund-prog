'''
Faça um programa que preencha três listas com dez posições cada um: a primeira lista, com os nomes de dez produtos; a segunda lista, com os códigos dos dez produtos; e a terceira lista, com os preços dos produtos. Mostre um relatório apenas com o nome, o código, o preço e o novo preço dos produtos que sofrerão aumento.

Sabe-se que os produtos que sofrerão aumento são aqueles que possuem código par ou preço superior a R$ 1.000,00. Sabe-se ainda que, para os produtos que satisfazem as duas condições anteriores, código e preço, o aumento será de 20%; para aqueles que satisfazem apenas a condição de código, o aumento será de 15%; e para aqueles que satisfazem apenas a condição de preço, o aumento será de 10%.
'''

produtos = []
codigos = []
precos = []

for i in range(10):
    nome_produto = input("Digite o nome do produto: ")
    produtos.append(nome_produto)

    codigo_produto = int(input("Digite o código do produto [0000]: "))
    codigos.append(codigo_produto)

    preco_produto = float(input("Digite o preço do produto: R$ "))
    precos.append(preco_produto)

print("\nRELATÓRIO DE PRODUTOS COM AUMENTO")
print("-" * 35)

for i in range(10):
    codigo_par = codigos[i] % 2 == 0
    preco_maior_1000 = precos[i] > 1000

    if codigo_par and preco_maior_1000:
        novo_preco = precos[i] * 1.20
        print(f"Produto: {produtos[i]}")
        print(f"Código: {codigos[i]}")
        print(f"Preço atual: R$ {precos[i]:.2f}")
        print(f"Novo preço: R$ {novo_preco:.2f}")
        print("--------------------------------")
    
    elif codigo_par:
        novo_preco = precos[i] * 1.15
        print(f"Produto: {produtos[i]}")
        print(f"Código: {codigos[i]}")
        print(f"Preço atual: R$ {precos[i]:.2f}")
        print(f"Novo preço: R$ {novo_preco:.2f}")
        print("--------------------------------")
    
    elif preco_maior_1000:
        novo_preco = precos[i] * 1.10
        print(f"Produto: {produtos[i]}")
        print(f"Código: {codigos[i]}")
        print(f"Preço atual: R$ {precos[i]:.2f}")
        print(f"Novo preço: R$ {novo_preco:.2f}")
        print("--------------------------------")
        