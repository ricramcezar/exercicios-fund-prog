'''
Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
'''

# Python possui uma biblioteca nativa focada em matemática chamada math. Dentro dela, existe a função math.sqrt() (abreviação de square root). Para usá-la é preciso fazer um import math na primeira linha do seu arquivo.

# import math

cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))
soma_dos_quadrados = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = soma_dos_quadrados ** 0.5 # OU --> hipotenusa = math.sqrt(soma_dos_quadrados)

print(f"\nO valor da hipotenusa é {hipotenusa:.2f}.")