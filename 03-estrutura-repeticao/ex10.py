'''
Faça um programa que receba dez números, calcule e mostre a soma dos números pares e a soma dos números primos.
'''
import sys

TOTAL_NUMEROS = 10
soma_num_pares = 0
soma_num_primos = 0

for i in range(TOTAL_NUMEROS):
    
    while True:
        try:
            entrada = input(f"Digite o {i+1}º número inteiro positivo (ou [S] para sair): ").upper()
            if entrada == 'S': 
                sys.exit("Programa encerrado.")
            numero = int(entrada)
            if numero >= 0: 
                break
            print("Erro: Digite um número positivo.")
        except ValueError:
            print("Erro: Entrada inválida.")

    # --- SOMA DOS PARES ---
    if numero % 2 == 0:
        soma_num_pares += numero

    # --- LÓGICA DOS PRIMOS ---
    if numero > 1:
        e_primo = True
        # Verificando se existe algum divisor entre 2 e o próprio número
        for divisor in range(2, numero):
            if numero % divisor == 0:
                e_primo = False
                break # Se encontrou um divisor, já sei que não é primo, posso parar
        
        if e_primo:
            soma_num_primos += numero

print(f"\nSoma dos números pares: {soma_num_pares}")
print(f"Soma dos números primos: {soma_num_primos}")