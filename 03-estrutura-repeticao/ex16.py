'''
Faça um programa que receba várias idades, calcule e mostre a média das idades digitadas. Finalize digitando idade igual a zero.
'''

print("--- Sistema de Média de Idades ---")
print("Digite as idades uma a uma. Para encerrar e ver a média, digite 0.")
print("-" * 34)

soma_idades = 0
contador = 0

idade = int(input("Digite a idade: (ou 0 para sair): "))

while idade != 0:
    soma_idades += idade
    contador += 1
    idade = int(input("Digite a próxima idade (ou 0 para sair): "))

print("\nCalculando as médias das idades informadas...\n")

if contador > 0:
    media_idades = soma_idades / contador
    print(f"A média das {contador} idades digitadas é: {media_idades:.2f}\n")
else:
    print("Nenhuma idade válida foi informada.\n")