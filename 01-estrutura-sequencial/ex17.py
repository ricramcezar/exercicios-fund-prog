'''
Faça um programa que receba o raio, calcule e mostre:
a) o comprimento de uma esfera; sabe-se que C = 2 * πR;
b) a área de uma esfera; sabe-se que A = 4πR²;
c) o volume de uma esfera; sabe-se que V = 4/3 * πR³.
'''

# Para declarar π em Python, a forma mais precisa e comum é importar o módulo math e usar math.pi.

import math

raio = float(input("Digite o raio da esfera em cm: "))
valor_pi = math.pi
comprimento_esfera = 2 * valor_pi * raio
area_esfera = 4 * valor_pi * (raio ** 2)
volume_esfera = (4 / 3) * (valor_pi) * (raio ** 3)

print(f"A esfera com {raio}cm de raio tem {comprimento_esfera:.2f}cm de comprimento, {area_esfera:.2f}cm² de área e {volume_esfera:.2f}cm³ de volume.")