'''
Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui. Ela vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. Sabe-se que a cotação do dólar é de R$ 1,80; do marco alemão, de R$ 2,00; e da libra esterlina, de R$ 3,57. O programa deve fazer as conversões e mostrá-las.
'''

valor_para_viajar = float(input("Digite o valor que a pessoa possui (em reais): R$"))
converte_dolar = valor_para_viajar / 1.8
converte_marco = valor_para_viajar / 2.0
converte_libra = valor_para_viajar / 3.57

print()
print(f"O valor de R${valor_para_viajar:.2f} equivale a:\n"
      f"\n  {converte_dolar:.2f} dólares\n"
      f"  {converte_marco:.2f} marcos\n"
      f"  {converte_libra:.2f} libras")

print("\nBoa viagem!")