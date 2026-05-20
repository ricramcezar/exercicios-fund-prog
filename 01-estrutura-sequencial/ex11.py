'''
Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor)/2.
'''

diagonal_maior = float(input("\nDigite o valor da diagonal maior: "))
diagonal_menor = float(input("Digite o valor da diagonal menor: "))
area_losango = (diagonal_maior * diagonal_menor) / 2

print(f"\nA área do losango é {area_losango}cm².")