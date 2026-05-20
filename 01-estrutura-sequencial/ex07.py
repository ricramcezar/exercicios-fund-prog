'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.
'''

peso = float(input("Digite o peso em kg: "))
novo_peso_gordo = peso + peso * 0.15
novo_peso_magro = peso - peso * 0.2

print(f"O peso digitado foi {peso}.\n"
      f"Se a pessoa engordar 15%, pesará {novo_peso_gordo}kg.\n"
      f"Se a pessoa emagrecer 20%, pesará {novo_peso_magro}kg.")