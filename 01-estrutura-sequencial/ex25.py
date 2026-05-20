'''
Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos.
'''

hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))

hora_em_min = hora * 60
total_minutos = minutos + hora_em_min
min_em_seg = total_minutos * 60

print()
print(f"Hora convertida em minutos: {hora} horas são {hora_em_min} minutos.\n"
      f"Total de minutos (digitados + conversão): {total_minutos} é o total de minutos.\n"
      f"Minutos convertidos em segundos: {total_minutos} minutos são {min_em_seg} segundos.\n")