'''
Faça um programa que receba dois números e mostre o maior.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
  print(f"{num1} é maior que {num2}.")
else:
  print(f"{num2} é maior que {num1}.")