'''
Faça um programa que mostre as tabuadas dos números de 1 a 10.
'''

for numero_tabuada in range(1, 11):
    print(f"--- Tabuada do {numero_tabuada} ---")
    for multiplicador in range(0, 11):
        print(f"{numero_tabuada} x {multiplicador} = {numero_tabuada * multiplicador}")
    if numero_tabuada < 10:
        input("\nPressione Enter para continuar...")

    