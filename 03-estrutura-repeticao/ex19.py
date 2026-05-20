'''
Faça um programa que receba o tipo da ação, ou seja, uma letra a ser comercializada na bolsa de valores, o preço de compra e o preço de venda de cada ação e que calcule e mostre:
-> o lucro de cada ação comercializada;
-> a quantidade de ações com lucro superior a R$ 1.000,00;
-> a quantidade de ações com lucro inferior a R$ 200,00;
-> o lucro total da empresa.
Finalize com o tipo de ação ‘F’.
'''

acao_lucro_superior_mil = 0
acao_lucro_inferior_200 = 0
lucro_total = 0

while True:
    tipo_acao = input("Digite uma letra a ser comercializada na bolsa de valores (ou F para finalizar): ").strip().upper()
    if tipo_acao == "F":
        break
    preco_compra = float(input("Digite o preço de compra: R$ "))
    preco_venda = float(input("Digite o preço de venda: R$ "))
    lucro = preco_venda - preco_compra
    print(f"Lucro da ação {tipo_acao}: R$ {lucro:.2f}")

    if lucro > 1000:
        acao_lucro_superior_mil += 1
    
    if lucro < 200:
        acao_lucro_inferior_200 += 1
    
    lucro_total += lucro

print(f"Quantidade de ações com lucro superior a R$ 1.000,00: {acao_lucro_superior_mil} ações")
print(f"Quantidade de ações com lucro inferior a R$ 200,00: {acao_lucro_inferior_200} ações")
print(f"Lucro total da empresa: R$ {lucro_total:.2f}")