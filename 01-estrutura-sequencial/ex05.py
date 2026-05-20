'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
'''

preco = float(input("Digite o preço inicial: R$"))
desconto = 0.1
novo_preco = preco - preco * desconto

print(f"O novo preço, com desconto de 10%, é R${novo_preco}.")
