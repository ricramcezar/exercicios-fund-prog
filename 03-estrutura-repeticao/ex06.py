'''
Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:

a) o valor total das compras à vista;
b) o valor total das compras a prazo;
c) o valor total das compras efetuadas; e
d) o valor da primeira prestação das compras a prazo juntas, sabendo-se que serão pagas em três vezes.
'''
import sys

TOTAL_TRANSACOES = 15
total_avista = 0.00
total_aprazo = 0.00

for i in range(TOTAL_TRANSACOES):
    codigo = input("Digite [V] para transação à vista ou [P] para transação a prazo: ").upper()
    if codigo != "V" and codigo != "P":
        print("Código Inválido.")
        sys.exit()

    valor = float(input("Digite o valor da transação - use ponto [.] para centavos: R$"))

    if codigo == "V":
        total_avista += valor
    else:
        total_aprazo += valor
   

total_compras = total_avista + total_aprazo
primeira_prestacao = total_aprazo / 3

print(f"Total à vista: R$ {total_avista:.2f}\n"
      f"Total a prazo: R$ {total_aprazo:.2f}\n"
      f"Total das compras: R$ {total_compras:.2f}\n"
      f"Valor da primeira prestação: R$ {primeira_prestacao:.2f}\n")