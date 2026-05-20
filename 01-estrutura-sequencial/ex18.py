'''
Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180*(C + 32)/100.
'''

# Ou seja, F = (C * 1.8) + 32 --> C = (F - 32) / 1.8

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = (temp_celsius * 1.8) + 32

print(f"{temp_celsius:.2f}°C equivale a {temp_fahrenheit:.2f}°F.")