""" 
Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade de opção inválida e não se preocupe com as restrições como salário inválido.

Menu de opções:
1. Novo salário
2. Férias
3. Décimo terceiro
4. Sair
Digite a opção desejada.

Na opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a seguir:

SALÁRIOS                                PORCENTAGEM DE AUMENTO
Até R$210,00                            15%
de R$210,00 a R$600,00 (inclusive)      10%
Acima de R$600,00                       5%

Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor de suas férias. Sabe-se que as férias equivalem a seu salário acrescido de um terço do salário.

Na opção 3: receber o salário de um funcionário e o número de meses de trabalho na empresa, no máximo doze, calcular e mostrar o valor do décimo terceiro. Sabe-se que o décimo terceiro equivale a seu salário multiplicado pelo número de meses de trabalho dividido por 12.

Na opção 4: sair do programa.

"""

while True:
    print("===== MENU DE OPÇÕES =====\n")
    print("[1] - Novo salário\n"
          "[2] - Férias\n"
          "[3] - Décimo terceiro\n"
          "[4] - Sair\n")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        salario = float(input("Digite o salário: R$ "))
        if salario <= 210:
            novo_salario = salario + (salario * 0.15)
        elif salario <= 600:
            novo_salario = salario + (salario * 0.10)
        else: 
            novo_salario = salario + (salario * 0.05)
        print(f"\nO novo salário é R$ {novo_salario:.2f}\n")
    
    elif opcao == 2:
        salario = float(input("Digite o salário: R$ "))
        ferias = salario + (salario / 3)
        print(f"\nO valor das férias é: R$ {ferias:.2f}\n")
    
    elif opcao == 3:
        salario = float(input("Digite o salário: R$ "))
        meses_trabalhados = int(input("Digite a quantidade de meses trabalhados: "))
        decimo_terceiro = (salario * meses_trabalhados) / 12
        print(f"\nO décimo terceiro tem o valor de: R$ {decimo_terceiro:.2f}\n")
    
    elif opcao == 4:
        break

    else:
        print("\nOpção inválida. Tente novamente!\n")