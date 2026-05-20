'''
Faça um programa que receba dois números e execute uma das operações listadas a seguir, de acordo com a escolha do usuário. Se for digitada uma opção inválida, mostre mensagem de erro e termine a execução do programa. As opções são:
a) O primeiro número elevado ao segundo número.
b) Raiz quadrada de cada um dos números.
c) Raiz cúbica de cada um dos números.
'''
import sys
import math

while True:
  print("-" * 50)

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  print()
  print("Escolha dentre as opções abaixo:\n"
        "\na. O primeiro número elevado ao segundo número.\n"
        "b. Raiz quadrada de cada um dos números.\n"
        "c. Raiz cúbica de cada um dos números.\n")

  escolha_usuario = input("Digite 'a', 'b' ou 'c': ")
  opcoes = ["a", "b", "c"]

  if escolha_usuario not in opcoes:
    print("\nErro: Opção inválida!\n")
    acao = input("Digite [1] para Sair ou [2] para Reiniciar: ")

    if acao == "1":
      print("Encerrando o programa...")
      sys.exit()
    else:
      print("Reiniciando...\n")
      continue # Ignora tudo abaixo e volta para o topo do 'while'

  elif escolha_usuario == "a":
    print(f"\n{num1} elevado a {num2} é igual a {num1 ** num2}.\n")
    break # O programa funcionou, então quebramos o loop para encerrar!

  elif escolha_usuario == "b":
    if num1 < 0 or num2 < 0:
      print("Erro: Não é possível calcular raiz quadrada de número negativo.")
      acao = input("Digite [1] para Sair ou [2] para Reiniciar: ")

      if acao == "1":
        print("Encerrando o programa...")
        sys.exit()
      else:
        print("Reiniciando...\n")
        continue # Volta para o topo do 'while'

    else:
      print(f"\nA raiz quadrada de {num1} é {math.sqrt(num1):.2f}.\n"
            f"A raiz quadrada de {num2} é {math.sqrt(num2):.2f}.\n")
      break # Conta feita com sucesso, encerra o loop
  elif escolha_usuario == "c":
    print(f"\nA raiz cúbica de {num1} é {math.cbrt(num1):.2f}.\n"
          f"A raiz cúbica de {num2} é {math.cbrt(num2):.2f}.\n")
    break # Conta feita com sucesso, encerra o loop