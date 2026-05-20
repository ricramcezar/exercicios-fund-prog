'''
Faça um programa que apresente o menu de opções a seguir:
Menu de opções:
1. Média aritmética
2. Média ponderada
3. Sair
Digite a opção desejada.
Na opção 1: receber duas notas, calcular e mostrar a média aritmética.
Na opção 2: receber três notas e seus respectivos pesos, calcular e mostrar a média ponderada.
Na opção 3: sair do programa.
Verifique a possibilidade de opção inválida. Nesse caso, o programa deverá mostrar uma mensagem.
'''

while True:
    print("-" * 18)
    print("Menu de opções")
    print("-" * 18)
    print("1. Média aritmética\n"
          "2. Média ponderada\n"
          "3. Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media_aritmetica = (nota1 + nota2) / 2
        print(f"A média aritmética de {nota1} e {nota2} é {media_aritmetica:.2f}")
    elif opcao == 2:
        nota1 = float(input("Digite a primeira nota: "))
        peso1 = float(input("Digite o peso desta nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        peso2 = float(input("Digite o peso desta nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        peso3 = float(input("Digite o peso desta nota: "))
        pesos = peso1 + peso2 + peso3
        if pesos == 0:
            print("A soma dos pesos não pode ser zero.")
            break
        media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / pesos
        print(f"A média ponderada das três notas é {media_ponderada:.1f}")
    elif opcao == 3:
        break
    else:
        print("\nERRO: OPÇÃO INVÁLIDA. TENTE NOVAMENTE!\n")