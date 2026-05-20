'''
Faça um programa que leia cinco grupos de quatro valores (A, B, C, D) e mostre-os na ordem lida. Em seguida, organize-os em ordem crescente e decrescente.
'''
# O 'for' cria o ciclo. 'grupo' vai valer 0, depois 1, 2, 3 e 4.
for grupo in range(5):
    print(f"\n--- Lendo o Grupo {grupo + 1} ---")
    
    # 1. Recebendo os 4 valores e guardando em uma lista
    # Vou usar a "Opção 1" que é mais clara para quem está começando
    a = float(input("Digite o valor A: "))
    b = float(input("Digite o valor B: "))
    c = float(input("Digite o valor C: "))
    d = float(input("Digite o valor D: "))
    
    valores = [a, b, c, d]
    
    # 2. Mostrando na ordem lida
    print(f"Ordem lida: {valores}")
    
    # 3. Organizando em ordem crescente
    valores.sort() 
    print(f"Crescente:  {valores}")
    
    # 4. Organizando em ordem decrescente
    valores.sort(reverse=True)
    print(f"Decrescente: {valores}")

print("\nFim do programa! Todos os 5 grupos foram processados.")