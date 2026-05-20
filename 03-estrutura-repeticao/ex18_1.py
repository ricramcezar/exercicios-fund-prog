'''
Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:

-> a média dos salários do grupo;
-> a maior e a menor idade do grupo;
-> a quantidade de mulheres com salário até R$ 200,00;
-> a idade e o sexo da pessoa que possui o menor salário.

Finalize a entrada de dados ao ser digitada uma idade negativa.
'''
lista_salarios = []
qtd_mulheres_200 = 0
idades = []
sexos = []

while True:
    idade = int(input("Digite a idade (ou uma idade negativa para sair): "))
    if idade < 0:
        break
    idades.append(idade)
    sexo = input("Digite [M] para masculino ou [F] para feminino: ").upper()
    sexos.append(sexo)
    salario = float(input("Digite o salário (para centavos, use ponto[.] - ex. R$ 450.75): R$ "))
    lista_salarios.append(salario)
    if sexo == "F" and salario <= 200:
        qtd_mulheres_200 += 1

if len(idades) > 0:
    media_salarios = (sum(lista_salarios) / len(lista_salarios))
    maior_idade = max(idades)
    menor_idade = min(idades)
    menor_salario = min(lista_salarios)
    indice_menor_salario = lista_salarios.index(menor_salario)
    idade_menor_salario = idades[indice_menor_salario]
    sexo_menor_salario = sexos[indice_menor_salario]
    print("--- RESULTADO FINAL ---")
    print(f"Média dos salários do grupo: R$ {media_salarios:.2f}\n"
        f"Maior idade do grupo: {maior_idade} anos\n"
        f"Menor idade do grupo: {menor_idade} anos\n"
        f"Mulheres com salário até R$ 200.00: {qtd_mulheres_200}\n"
        f"Idade da pessoa com menor salário: {idade_menor_salario} anos\n"
        f"Sexo da pessoa com menor salário: {sexo_menor_salario}")
    print("-" * 20)
else:
    print("Nenhum dado foi cadastrado.")

    