'''
Faça um programa que preencha uma lista com dez números inteiros e uma segunda lista com cinco números inteiros, calcule e mostre duas listas resultantes. A primeira lista resultante será composta pela soma de cada número par da primeira lista somado a todos os números da segunda lista. A segunda lista resultante será composta pela quantidade de divisores que cada número ímpar da primeira lista tem na segunda lista.
'''

lista01 = []
lista02 = []

for i in range(10):
    numero1 = int(input("Digite um número inteiro: "))
    lista01.append(numero1)

for i in range(5):
    numero2 = int(input("Digite outro número inteiro: "))
    lista02.append(numero2)

lista_result1 = []
lista_result2 = []

soma_lista02 = sum(lista02)

for numero in lista01:
    if numero % 2 == 0:
        resultado = numero + soma_lista02
        lista_result1.append(resultado)
    else:
        contador_divisores = 0

        for divisor in lista02:
            if divisor != 0 and numero % divisor == 0:
                contador_divisores += 1
        
        lista_result2.append(contador_divisores)

print(f"Primeira lista resultante: {lista_result1}")
print(f"Segunda lista resultante: {lista_result2}")