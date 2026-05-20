'''
Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas, calcule e mostre o salário a receber, de acordo com as regras a seguir:
a) a hora trabalhada vale 1/8 do salário mínimo;
b) a hora extra vale 1/4 do salário mínimo;
c) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
d) a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra;
e) o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras.
'''

# Entrada de dados (agora recebendo também o salário mínimo)
salario_minimo = float(input("Digite o valor do salário mínimo: R$ "))
num_horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
num_horas_extras = float(input("Digite o número de horas extras trabalhadas: "))

# Processamento
valor_hora_trabalhada = salario_minimo / 8
valor_hora_extra = salario_minimo / 4

salario_bruto = num_horas_trabalhadas * valor_hora_trabalhada
quantia_horas_extras = num_horas_extras * valor_hora_extra
salario_receber = salario_bruto + quantia_horas_extras

# Saída de dados
print()
print("-" * 100)
print(f"Neste mês o funcionário trabalhou {num_horas_trabalhadas} horas regulares e fez {num_horas_extras} horas extras.")
print("-" * 100)
print(f"Horas trabalhadas: {num_horas_trabalhadas}\n"
      f"Horas extras: {num_horas_extras}\n"
      f"A receber (horas trabalhadas): R${salario_bruto:.2f}\n" 
      f"A receber (horas extras): R${quantia_horas_extras:.2f}\n"
      f"Salário bruto: R${salario_bruto:.2f}\n"
      f"Salário total a receber: R${salario_receber:.2f}\n")