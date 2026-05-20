'''
Uma agência bancária possui vários clientes que podem fazer investimentos com rendimentos mensais, conforme a tabela a seguir:

TIPO    DESCRIÇÃO               RENDIMENTO MENSAL
1       Poupança                1,5%
2       Poupança plus           2%
3       Fundos de renda fixa    4%

Faça um programa que leia o código do cliente, o tipo do investimento e o valor investido, e que calcule e mostre o rendimento mensal de acordo com o tipo do investimento. No final o programa deverá mostrar o total investido e o total de juros pagos.

A leitura terminará quando o código do cliente digitado for menor ou igual a 0.

'''
total_investido = 0
total_juros_pagos = 0

while True:
    codigo_cliente = int(input("Digite o código do cliente: "))
    
    if codigo_cliente <= 0:
        break
    
    print("\n=== TIPOS DE INVESTIMENTO ===\n"
          "[1] - Poupança\n"
          "[2] - Poupança plus\n"
          "[3] - Fundos de renda fixa\n")
    
    tipo_investimento = int(input("Digite o tipo de investimento desejado: "))
    
    if tipo_investimento < 1 or tipo_investimento > 3:
        print("Tipo de investimento inválido. Tente novamente.")
        continue
    
    valor_investido = float(input("Digite o valor a investir: R$ "))
    
    if valor_investido <= 0: 
        print("Valor inválido. O investimento deve ser maior que zero.")
        continue
    
    if tipo_investimento == 1:
        rendimento = valor_investido * 0.015
    elif tipo_investimento == 2:
        rendimento = valor_investido * 0.02
    else:
        rendimento = valor_investido * 0.04
    
    total_investido += valor_investido
    total_juros_pagos += rendimento

    print(f"\nCódigo do cliente: {codigo_cliente}")
    print(f"Valor investido: R$ {valor_investido:.2f}")
    print(f"Rendimento mensal: R$ {rendimento:.2f}")

print("\n=== RESUMO FINAL ===")
print(f"Total investido: R$ {total_investido:.2f}")
print(f"Total de juros pagos: R$ {total_juros_pagos:.2f}\n")
           