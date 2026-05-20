'''
Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2, deve-se usar 18 W de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros), calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.
'''

base_comodo = float(input("Digite o valor da base do cômodo em metros: "))
altura_comodo = float(input("Digite o valor da altura do cômodo em metros: "))
area_comodo = base_comodo * altura_comodo
potencia = area_comodo * 18

print(f"\nPara iluminar um cômodo de {area_comodo:.2f}m², são necessários {potencia:.2f}W de potência.")