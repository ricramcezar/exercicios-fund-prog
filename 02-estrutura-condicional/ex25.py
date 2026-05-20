'''
Uma empresa decidiu dar uma gratificação de Natal a seus funcionários, baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:

H = número de horas extras - (2/3 * (número de horas falta))

H (MINUTOS)                     PRÊMIO (R$)
>= 2400                         500
> 1800 e < 2400                 400
>= 1200 e < 1800                300
>= 600 e < 1200                 200
< 600
'''

import sys

try:
    horas_extras = int(input("Digite a quantidade de horas extras trabalhadas: "))
    horas_falta = int(input("Digite a quantidade de horas falta: "))
except ValueError:
    print("Digite apenas números de horas.")
    sys.exit()

if horas_extras < 0 or horas_falta < 0:
    print("Erro: Digite apenas números positivos.")
    sys.exit()

horas = horas_extras - ((2 / 3) * horas_falta)
minutos = horas * 60

if minutos >= 2400:
    premio = 500
elif minutos >= 1800:
    premio = 400
elif minutos >= 1200:
    premio = 300
elif minutos >= 600:
    premio = 200
else:
    premio = 100

print("\n" + "="*35)
print(f"VALOR H (Horas):   {horas:.2f}")
print(f"VALOR H (Minutos): {minutos:.2f}")
print("-" * 35)
print(f"PRÊMIO DE NATAL:   R$ {premio:.2f}")
print("="*35 + "\n")