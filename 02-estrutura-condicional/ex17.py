'''
Faça um programa que verifique a validade de uma senha fornecida pelo usuário. A senha é 4531. O programa deve mostrar uma mensagem de permissão de acesso ou não.
'''

# Definindo a senha como uma constante para facilitar mudanças futuras
SENHA_CORRETA = "4531"

entrada = input("Digite a senha (4 números): ")

# Validação de formato (comprimento e se são apenas números)
if len(entrada) != 4 or not entrada.isdigit():
    print("Erro: A entrada deve possuir exatamente quatro números.")
else:
    # Verificação da validade
    if entrada == SENHA_CORRETA:
        print("Senha correta. Acesso permitido")
    else:
        print("Senha incorreta. Acesso negado")