'''
Faça um programa que preencha uma lista com quinze elementos inteiros e verifique a existência de elementos iguais a 30, mostrando as posições em que apareceram.
'''

elementos = []

for i in range(15):
    numero = int(input("Digite um número inteiro: "))
    elementos.append(numero)

for posicao, valor in enumerate(elementos):
    if valor == 30:
        print(f"O número 30 aparece na posição {posicao + 1}")