'''
Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180 graus.
'''

angulo1 = int(input("Digite o valor do primeiro ângulo: "))
angulo2 = int(input("Digite o valor do segundo ângulo: "))

angulo3 = 180 - angulo1 - angulo2

print(f"\nUm triângulo de ângulos {angulo1} graus e {angulo2} graus possui um terceiro ângulo de {angulo3} graus.\n")