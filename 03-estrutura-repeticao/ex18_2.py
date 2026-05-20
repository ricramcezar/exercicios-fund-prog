'''
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:

-> a média dos salários do grupo;
-> a maior e a menor idade do grupo;
-> a quantidade de mulheres com salário até R$ 200,00;
-> a idade e o sexo da pessoa que possui o menor salário.

Finalize a entrada de dados ao ser digitada uma idade negativa.
'''
qtd_pessoas = 0
soma_salarios = 0
qtd_mulheres_200 = 0

maior_idade = None
menor_idade = None

menor_salario = None
idade_menor_salario = None
sexo_menor_salario = None

while True:
    idade = int(input("Digite a idade (ou uma idade negativa para sair): "))

    if idade < 0:
        break

    sexo = input("Digite [M] para masculino ou [F] para feminino: ").upper()
    salario = float(input("Digite o salário (para centavos, use ponto[.] - ex. R$ 450.75): R$ "))

    qtd_pessoas += 1
    soma_salarios += salario

    if qtd_pessoas == 1:
        maior_idade = idade
        menor_idade = idade
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo
    else:
        if idade > maior_idade:
            maior_idade = idade

        if idade < menor_idade:
            menor_idade = idade

        if salario < menor_salario:
            menor_salario = salario
            idade_menor_salario = idade
            sexo_menor_salario = sexo

    if sexo == "F" and salario <= 200:
        qtd_mulheres_200 += 1

if qtd_pessoas > 0:
    media_salarios = soma_salarios / qtd_pessoas

    print("--- RESULTADO FINAL ---")
    print(f"Média dos salários do grupo: R$ {media_salarios:.2f}")
    print(f"Maior idade do grupo: {maior_idade} anos")
    print(f"Menor idade do grupo: {menor_idade} anos")
    print(f"Mulheres com salário até R$ 200,00: {qtd_mulheres_200}")
    print(f"Idade da pessoa com menor salário: {idade_menor_salario} anos")
    print(f"Sexo da pessoa com menor salário: {sexo_menor_salario}")
    print("-" * 20)
else:
    print("Nenhum dado foi cadastrado.")