'''
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h é a altura):
-> para homens: (72.7 * h) - 58.
-> para mulheres: (62.1 * h) - 44.7
'''

import sys

# Entrada de dados
try:
    altura_cm = float(input("Digite a sua altura em cm (ex.: 175): "))
    sexo = input("Digite [M] para masculino ou [F] para feminino: ").strip().upper()
    # strip() remove espaços acidentais que o usuário possa digitar antes ou depois da letra.
except ValueError:
    print("Erro: A altura deve ser um valor numérico.")
    sys.exit()

# Validação lógica
if altura_cm <= 0:
    print("Erro: Altura deve ser maior que zero.")
    sys.exit()

# Processamento com validação de entrada para o sexo
h = altura_cm / 100

if sexo == "M":
    peso_ideal = (72.7 * h) - 58
elif sexo == "F":
    peso_ideal = (62.1 * h) - 44.7
else:
    print("Erro: Opção de sexo inválida. Use apenas 'M' ou 'F'.")
    sys.exit()

# Saída formatada
print(f"\n--- Resultado ---")
print(f"Sexo: {'Masculino' if sexo == 'M' else 'Feminino'}")
print(f"Altura: {h:.2f}m")
print(f"Seu peso ideal calculado é: {peso_ideal:.2f} kg\n")
