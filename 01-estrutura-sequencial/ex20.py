'''
Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e a distância em que a escada está da parede, calcule e mostre a medida da escada para que se possa alcançar sua ponta.
'''

import math

angulo_graus = float(input("Digite a medida do ângulo formado (em graus): "))
angulo_radianos = math.radians(angulo_graus)
distancia_escada = float(input("Digite a distância da base da escada até a parede (em cm): "))
medida_escada = distancia_escada / math.cos(angulo_radianos)

print(f"A escada tem {medida_escada:.2f}cm de medida.")