'''
Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A — azul; P — preto; V — verde; e C — castanho) e a cor dos cabelos (P — preto; C — castanho; L — louro; e R — ruivo) de seis pessoas, e que calcule e mostre:
a) a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 kg;
b) a média das idades das pessoas com altura inferior a 1,50 m;
c) a porcentagem de pessoas com olhos azuis entre todas as pessoas analisadas; e
d) a quantidade de pessoas ruivas e que não possuem olhos azuis.
'''

import sys

TOTAL_PESSOAS = 6

qtd_50_60kg = 0
soma_idades_altura_150 = 0
qtd_altura_150 = 0
qtd_olhos_azuis = 0
qtd_ruivas_sem_azul = 0

print(input("\nVocê fornecerá as seguintes informações de seis pessoas diferentes: idade, peso, altura, cor dos olhos e cor dos cabelos.\nPressione [Enter] para iniciar:"))

for i in range(TOTAL_PESSOAS):
    print(f"\n--- Dados da Pessoa {i + 1} ---")

    # --- VALIDAÇÃO DA IDADE ---
    while True:
        entrada = input("Digite a idade (ou [S] para sair): ").upper()
        if entrada == "S":
            print("Programa encerrado pelo usuário.")
            sys.exit()
        
        try:
            idade = int(entrada)
            if idade >= 0:
                break
            else:
                print("Erro: Digite um número positivo.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número ou [S] para sair.")
        
    # --- VALIDAÇÃO DO PESO ---
    while True:
        entrada = input("Digite o peso em kg - use ponto [.] para gramas (ou [S] para sair): ").upper()
        if entrada == "S":
            sys.exit("Programa encerrado pelo usuário.")
        
        try:
            peso = float(entrada)
            if peso > 0:
                break
            else:
                print("Erro: O peso deve ser maior que zero.")
        except ValueError:
            print("Erro: Use ponto [.] para decimais (ex: 70.5)")
    
    # --- VALIDAÇÃO DA ALTURA ---

    while True:
        entrada = input("Digite a altura em cm (ex: 175) (ou [S] para sair): ").upper()
        if entrada == "S":
            sys.exit("Programa encerrado pelo usuário.")
        
        try:
            altura_cm = int(entrada)
            if altura_cm > 0:
                altura_m = altura_cm / 100 # Convertendo para metros
                break
            else:
                print("Erro: A altura deve ser maior que zero.")
        except ValueError:
            print("Erro: Use apenas números inteiros para cm.")
    
    # --- VALIDAÇÃO DA COR DOS OLHOS ---
    while True:
        olhos = input("Cor dos olhos\n[A-Azul, P-Preto, V-Verde, C-Castanho] (ou [S] para sair): ").upper()
        if olhos == "S":
            sys.exit("Programa encerrado pelo usuário.")
        if olhos in ["A", "P", "V", "C"]:
            break
        print("Erro: Opção inválida! Escolha entre A, P, V ou C.")

    # --- VALIDAÇÃO DA COR DOS CABELOS ---
    while True:
        cabelos = input("Cor dos cabelos\n[P-Preto, C-Castanho, L-Louro, R-Ruivo] (ou [S] para sair): ").upper()
        if cabelos == "S":
            sys.exit("Programa encerrado pelo usuário.")
        if cabelos in ["P", "C", "L", "R"]:
            break
        print("Erro: Opção inválida! Escolha entre P, C, L ou R.")
    
    # --- PROCESSAMENTO DOS DADOS (Cálculos por pessoa) ---
    if idade > 50 and peso < 60:
        qtd_50_60kg += 1
    
    if altura_m < 1.50:
        soma_idades_altura_150 += idade
        qtd_altura_150 += 1
    
    if olhos == "A":
        qtd_olhos_azuis += 1
    
    if cabelos == "R" and olhos != "A":
        qtd_ruivas_sem_azul += 1
    
# --- EXIBIÇÃO DOS RESULTADOS ---
print("\n" + "=" * 30)
print("RELATÓRIO FINAL")
print(f"a) Pessoas > 50 anos e < 60 kg: {qtd_50_60kg}")

if qtd_altura_150 > 0:
    media = soma_idades_altura_150 / qtd_altura_150
    print(f"b) Média das idades (altura < 1.50m): {media:.2f}")
else:
    print("b) Ninguém com altura inferior a 1.50m.")

porcentagem_azul = (qtd_olhos_azuis / TOTAL_PESSOAS) * 100
print(f"c) Porcentagem de olhos azuis: {porcentagem_azul:.2f}%")
print(f"d) Ruivas sem olhos azuis: {qtd_ruivas_sem_azul}")