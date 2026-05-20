'''
Uma companhia de teatro deseja montar uma série de espetáculos. A direção calcula que, a R$ 5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão de R$ 200,00. Diminuindo-se em R$ 0,50 o preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos. Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse preço de R$ 5,00 a R$ 1,00, de R$ 0,50 em R$ 0,50. Escreva, ainda, para cada novo preço de ingresso, o lucro máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.
'''

preco_inicial = 5.00
qtde_inicial = 120
desconto = 0.50
aumento_vendas = 26
despesa_fixa = 200
lucro_maximo = -9999
melhor_preco = 0
melhor_qtde = 0

while preco_inicial >= 1.00:
    lucro_atual = (preco_inicial * qtde_inicial) - despesa_fixa
    print(f"Preço: {preco_inicial:.2f} | Vendas: {qtde_inicial} | Lucro: {lucro_atual:.2f}")
    if lucro_atual > lucro_maximo:
        lucro_maximo = lucro_atual
        melhor_preco = preco_inicial
        melhor_qtde = qtde_inicial
    preco_inicial -= 0.50
    qtde_inicial += 26

print(f"Lucro máximo esperado: R$ {lucro_maximo:.2f}\n"
      f"Preço do ingresso: R$ {melhor_preco:.2f}\n"
      f"Ingressos vendidos: {melhor_qtde}")