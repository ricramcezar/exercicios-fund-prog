'''
Faça um programa para controlar o estoque de mercadorias de uma empresa. Inicialmente, o programa deverá preencher duas listas com dez posições cada, onde a primeira corresponde ao código do produto e a segunda, ao total desse produto em estoque. Logo após, o programa deverá ler um conjunto indeterminado de dados contendo o código de um cliente e o código do produto que ele deseja comprar, juntamente com a quantidade. Código do cliente igual a zero indica fim do programa. O programa deverá verificar:

-> se o código do produto solicitado existe. Se existir, tentar atender ao pedido; caso contrário, exibir mensagem "Código inexistente";
-> cada pedido feito por um cliente só pode ser atendido integralmente. Caso isso não seja possível, escrever a mensagem "Não temos estoque suficiente dessa mercadoria". Se puder atendê-lo, escrever a mensagem "Pedido atendido. Obrigado e volte sempre";
-> efetuar a atualização do estoque somente se o pedido for atendido integralmente;
-> no final do programa, escrever os códigos dos produtos com seus respectivos estoques já atualizados.
'''

codigo_produto = []
total_em_estoque = []

for i in range(10):
    codigo = input("Digite o código do produto [XX0000]: ")
    codigo_produto.append(codigo)
    quantidade = int(input("Digite a quantidade do produto: "))
    total_em_estoque.append(quantidade)

while True:
    codigo_cliente = int(input("Digite o código do cliente: "))
    if codigo_cliente == 0:
        break
    else:
        produto_desejado = input("Digite o código do produto desejado [XX0000]: ")
        quantidade_desejada = int(input("Digite a quantidade desejada: "))
        if produto_desejado not in codigo_produto:
            print("Código inexistente")
        else:
            posicao = codigo_produto.index(produto_desejado)
            estoque_disponivel = total_em_estoque[posicao]
            if quantidade_desejada > estoque_disponivel:
                print("Não temos estoque suficiente dessa mercadoria")
            else:
                total_em_estoque[posicao] = estoque_disponivel - quantidade_desejada
                print("Pedido atendido. Obrigado e volte sempre.")

for i in range(len(codigo_produto)):
    print(f"{codigo_produto[i]}: {total_em_estoque[i]}")