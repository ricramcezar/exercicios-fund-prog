'''
Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário.

ESCOLHA DO USUÁRIO    OPERAÇÃO
1                     Média entre os números digitados
2                     Diferença do maior pelo menor
3                     Produto entre os números digitados
4                     Divisão do primeiro pelo segundo

Se a opção digitada for inválida, mostre uma mensagem de erro e termine a execução do programa. Lembre-se de que, na operação 4, o segundo número deve ser diferente de zero.
'''

import sys

# O 'while True' cria um ciclo que vai se repetir para sempre...
while True:
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  # Verificar se algum dos números é negativo
  if num1 < 0 or num2 < 0:
    print("\nErro: Por favor, digite somente números positivos. Vamos tentar de novo!\n")
    # Como não colocamos o comando 'break' aqui, o Python volta para a linha do 'while'
  else:
    break

# ...até que o 'break' seja acionado. Quando isso acontece, o programa continua daqui:

print()
print("Escolha uma operação:\n"
      "1. Média entre os números digitados\n"
      "2. Diferença do maior pelo menor\n"
      "3. Produto entre os números digitados\n"
      "4. Divisão do primeiro pelo segundo\n")
escolha_usuario = int(input("Digite 1-4: "))

if escolha_usuario < 1 or escolha_usuario > 4:
  print("\nErro: Opção inválida!\n")
  sys.exit()

if escolha_usuario == 1:
  print(f"A média entre os números {num1} e {num2} é {(num1 + num2) / 2}.")
elif escolha_usuario == 2:
  if num1 > num2:
    print(f"A diferença entre {num1} e {num2} é {num1 - num2}.")
  else:
    print(f"A diferença entre {num2} e {num1} é {num2 - num1}.")
elif escolha_usuario == 3:
  print(f"O produto entre {num1} e {num2} é {num1 * num2}.")
elif escolha_usuario == 4:
  if num2 == 0:
    print("\nErro: Não é possível dividir por 0.\n")
    sys.exit()
  else:
    print(f"A divisão de {num1} por {num2} é {round((num1 / num2), 2)}.")