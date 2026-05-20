'''
Faça um programa que calcule e mostre a área de um trapézio.
Sabe-se que: A = ((base maior + base menor) * altura)/2
'''

base_maior = float(input("\nDigite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))
area_trapezio = ((base_maior + base_menor) * altura) / 2

print(f"\nA área do trapézio é {area_trapezio}cm²")