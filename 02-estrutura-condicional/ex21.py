'''
Faça um programa que receba o preço de um produto e seu código de origem e mostre sua procedência. A procedência obedece à tabela a seguir.

CÓDIGO DE ORIGEM        PROCEDÊNCIA
1                       Sul
2                       Norte
3                       Leste
4                       Oeste
5 ou 6                  Nordeste
7 ou 8 ou 9             Sudeste
10 a 20                 Centro-oeste
21 a 30                 Nordeste
'''

import sys

# Configuração de instruções
print("\nForneça o preço do produto.")
print("Use um ponto [.] caso queira identificar os centavos.")

# Entrada de dados
try:
    preco_produto = float(input("Preço do produto: R$ "))
    codigo_origem = int(input("Digite o código de origem [1 a 30]: "))
except ValueError:
    print("Erro: O preço deve ser um número válido.")
    sys.exit()

# Validação lógica inicial
if codigo_origem <= 0:
    print("Erro: Digite apenas valores numéricos para preço e código.")
    sys.exit()

# Classificação
if codigo_origem == 1:
    procedencia = "Sul"
elif codigo_origem == 2:
    procedencia = "Norte"
elif codigo_origem == 3:
    procedencia = "Leste"
elif codigo_origem == 4:
    procedencia = "Oeste"
elif codigo_origem in [5, 6]:
    procedencia = "Nordeste"
elif codigo_origem in [7, 8, 9]:
    procedencia = "Sudeste"
elif codigo_origem <= 20:
    procedencia = "Centro-oeste"
elif codigo_origem <= 30:
    procedencia = "Centro-oeste"
else:
    procedencia = "Código fora do intervalo permitido"

# Exibição dos resultados

print("-" * 25)
print(f"Preço do produto: R$ {preco_produto:.2f}")
print(f"Procedência: {procedencia}")
print("-" * 25)