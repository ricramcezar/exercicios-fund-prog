'''
Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra na tabela a seguir:

Média Aritmética        Mensagem
-------------------------------------
0.0 <= n > 3.0          Reprovado
3.0 <= n > 7.0          Exame
7.0 <= n > 10.0         Aprovado
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media_notas = (nota1 + nota2) / 2
print(f"\nA média das notas é {media_notas:.1f}.")

if media_notas < 3:
  print("Resultado: Reprovado")
elif media_notas >= 3 and media_notas < 7:
  print("Resultado: Exame")
else:
  print("Resultado: Aprovado")