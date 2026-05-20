'''
Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado. Para isso, forneceu o sexo do entrevistado e sua resposta (S — sim; ou N — não). Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:
-> o número de pessoas que responderam sim;
-> o número de pessoas que responderam não;
-> o número de mulheres que responderam sim; e
-> a percentagem de homens que responderam não, entre todos os homens analisados.
'''

TOTAL_PESSOAS = 10

total_gostaram = 0
total_nao_gostaram = 0
mulheres_gostaram = 0
homens_total = 0
homens_nao_gostaram = 0

for i in range(TOTAL_PESSOAS):
    sexo = input("Digite [M] para masculino ou [F] para feminino: ").upper()
    resposta = input("Você gostou do produto? Digite [S] - sim ou [N] - não: ").upper()
    if sexo == "M":
        homens_total += 1
    
    if resposta == "S":
        total_gostaram += 1
        if sexo == "F":
            mulheres_gostaram += 1
    elif resposta == "N":
        total_nao_gostaram += 1
        if sexo == "M":
            homens_nao_gostaram += 1

print(f"Total de pessoas que responderam SIM: {total_gostaram}")
print(f"Total de pessoas que responderam NÃO: {total_nao_gostaram}")
print(f"Número de mulheres que responderam SIM: {mulheres_gostaram}")

if homens_total > 0:
    porcentagem_homens = (homens_nao_gostaram / homens_total) * 100
else:
    print("Nenhum homem respondeu 'não'.")