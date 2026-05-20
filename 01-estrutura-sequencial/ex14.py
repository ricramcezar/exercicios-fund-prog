'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.
'''

import datetime
ano_atual = datetime.datetime.now().year
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_meses * 365
idade_semana = idade_meses * 52

print(f"A pessoa tem {idade_anos} anos.\n"
      f"A pessoa tem {idade_meses} meses de vida.\n"
      f"A pessoa tem {idade_dias} dias de vida.\n"
      f"A pessoa tem {idade_semana} semanas de vida.")