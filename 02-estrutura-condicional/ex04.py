'''
Faça um programa que receba três números e mostre o maior.
'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
  print(f"{num1} é maior do que {num2} e {num3}.")
elif num2 > num1 and num2 > num3:
  print(f"{num2} é maior do que {num1} e {num2}.")
elif num3 > num1 and num3 > num2:
  print(f"{num3} é maior do que {num1} e {num2}.")
else:
  print("Verifique os números digitados. Eles não podem ser iguais.")