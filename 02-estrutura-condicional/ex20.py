'''
Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir. Para idade inferior a 5, deverá mostrar mensagem.

CATEGORIA       IDADE
Infantil        5 a 7
Juvenil         8 a 10
Adolescente     11 a 15
Adulto          16 a 30
Sênior          Acima de 30
'''

import sys

# Entrada de dados
try:
    idade_nadador = int(input("Digite a idade do nadador: "))
except ValueError:
    print("Erro: A idade deve ser um número inteiro.\n")
    sys.exit()

# Validação lógica inicial
if idade_nadador < 5:
    print("Aviso: O nadador deve ter pelo menos 5 anos para competir.\n")
    sys.exit()

# Classificação por faixas
if idade_nadador <= 7:
    categoria = "Infantil"
elif idade_nadador <= 10:
    categoria = "Juvenil"
elif idade_nadador <= 15:
    categoria = "Adolescente"
elif idade_nadador <= 30:
    categoria = "Adulto"
else:
    categoria = "Sênior"

# Exibição dos resultados
print(f"-" * 25)
print(f"IDADE: {idade_nadador} anos")
print(f"CATEGORIA: {categoria}")
print(f"-" * 25)