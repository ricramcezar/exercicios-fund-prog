'''
Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:

a) o preço final para compra à vista tem desconto de 20%;
b) a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60; e
c) os percentuais de acréscimo encontram-se na tabela a seguir.

QUANTIDADE          PERCENTUAL DE ACRÉSCIMO
DE PARCELAS         SOBRE O PREÇO FINAL
6                           3%
12                          6%
18                          9%
24                          12%
30                          15%
36                          18%
42                          21%
48                          24%
54                          27%
60                          30%
'''

valor_carro = float(input("Digite o valor do carro: R$ "))
valor_avista = valor_carro * 0.80

print(f"\nValor do carro: R$ {valor_carro:.2f} | Valor do carro à vista: R$ {valor_avista:.2f}")
print(f"{'Preço Final':<26} | {'Parcelas':<18} | {'Valor da Parcela':<26}")
print("-" * 100)

for i in range(6, 61, 6):
    percentual = i / 2
    preco_final = valor_carro * (1 + (percentual / 100))
    valor_parcela = preco_final / i
    
    print(f"Preço Final: R$ {preco_final:<12.2f} | Qtde. Parcelas: {i:<10} | Valor Parcela: R$ {valor_parcela:.2f}")