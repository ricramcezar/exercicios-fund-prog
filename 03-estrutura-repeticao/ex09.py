'''
Faça um programa que receba dez idades, pesos e alturas, calcule e mostre:
a) a média das idades das dez pessoas;
b) a quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro; e
c) a porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90m.
'''

import sys

TOTAL_PESSOAS = 10

soma_idades = 0
qtd_90kg_150 = 0
cont_190m = 0
cont_1030_190m = 0

print("Você fornecerá dados de 10 pessoas.\nPressione[ENTER] para iniciar:")
input()

for i in range(TOTAL_PESSOAS):
    print(f"\n--- Dados da Pessoa {i + 1} ---")

    # --- VALIDAÇÃO DA IDADE ---
    while True:
        entrada = input("Digite a idade (ou [S] para sair): ").upper()
        if entrada == "S":
            sys.exit("Programa encerrado pelo usuário.")
        
        try:
            idade = int(entrada)
            if idade >= 0:
                break
            print("Erro: Digite um número positivo.")
        except ValueError:
            print("Erro: Entrada inválida.")
        
    # --- VALIDAÇÃO DO PESO ---
    while True:
        entrada = input("Digite o peso em kg - use ponto [.] para gramas (ou [S] para sair): ").upper()
        if entrada == "S":
            sys.exit("Programa encerrado pelo usuário.")
        
        try:
            peso = float(entrada)
            if peso > 0:
                break
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

    soma_idades += idade

    if peso > 90 and altura_m < 1.50:
        qtd_90kg_150 += 1
    
    if altura_m > 1.90:
        cont_190m += 1
        if 10 <= idade <= 30:
            cont_1030_190m += 1

print("\n" + "=" * 30)
print("RELATÓRIO FINAL")

media_idade = soma_idades / TOTAL_PESSOAS
print(f"a) Média das idades: {media_idade:.1f} anos")
print(f"b) Pessoas com peso > 90kg e altura < 1.50m: {qtd_90kg_150}")

if cont_190m > 0:
    porcentagem = (cont_1030_190m / cont_190m) * 100
    print(f"c) Porcentagem de pessoas (10-30 anos) entre as maiores de 1.90m: {porcentagem:.1f}")
else:
    print("c) Ninguém com altura superior a 1.90 foi registrado.")
