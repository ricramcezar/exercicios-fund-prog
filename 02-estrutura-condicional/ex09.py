'''
Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio no último ano. Faça um programa que receba o saldo médio de um cliente e calcule o valor do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito.

SALDO MÉDIO                     PERCENTUAL
Acima de R$400                  30% do saldo médio
>= R$400 e < R$300              25% do saldo médio
>= R$300 e < R$200              20% do saldo médio
Até R$200                       10% do saldo médio
'''

saldo_medio = float(input("Digite o saldo médio do último ano: R$"))

if saldo_medio <= 0:
  print("Erro: Digite um saldo válido (maior que zero).")
elif saldo_medio > 400:
  credito = saldo_medio * 0.3
elif saldo_medio > 300: # O Python já sabe que é <= 400
  credito = saldo_medio * 0.25
elif saldo_medio > 200: # O Python já sabe que é <= 300
  credito = saldo_medio * 0.2
else:                   # O Python já sabe que sobrou apenas o <= 200
  credito = saldo_medio * 0.1

# O print aparece apenas uma vez, imprimindo o que a cascata decidiu!  
print(f"\nSaldo médio: R${saldo_medio:.2f}\n"
      f"Valor do crédito: R${credito:.2f}\n")