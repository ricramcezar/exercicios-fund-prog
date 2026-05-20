'''
Faça um programa que preencha uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.
'''
numeros = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

qtde_negativos = 0
soma_positivos = 0

for numero in numeros:
    if numero < 0:
        qtde_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"\nQuantidade de números negativos: {qtde_negativos}")
print(f"Soma dos números positivos: {soma_positivos:.2f}\n")