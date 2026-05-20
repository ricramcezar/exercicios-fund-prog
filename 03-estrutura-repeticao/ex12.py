'''
Faça um programa que receba dez números inteiros e mostre a quantidade de números primos dentre os números que foram digitados.
'''

TOTAL_NUMEROS = 10

numeros_primos = 0
nao_primos = 0

for i in range(TOTAL_NUMEROS):
    numero = int(input("Digite um número: "))
    e_primo = True # Começa acreditando que o número é primo

    if numero < 2:
        e_primo = False
    else:
        # Testando se existe algum divisor entre 2 e o próprio número
        for divisor in range(2, numero):
            if numero % divisor == 0:
                e_primo = False # Encontramos um divisor, então não é primo
                break # Já se sabe que não é, podemos parar e testar esse número
    
    if e_primo:
        numeros_primos += 1

print(f"Quantidade de números primos: {numeros_primos}")
