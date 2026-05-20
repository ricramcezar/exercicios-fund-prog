'''
Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação média 7.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media_notas = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\nA média das notas é {media_notas:.1f}")

if media_notas >= 7:
  print("Resultado: Aprovado")
else:
  print("Resultado: Reprovado")

print()