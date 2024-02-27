#4) Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria_preco = float(input("Qual é o preço da mercadoria? "))
porc_mercadoria = float(input("Qual foi o % de desconto"))

calc = (porc_mercadoria / 100) * mercadoria_preco
print(f"\nValor de Desconto {calc}")
calc = mercadoria_preco - calc
print(f"Valor a pagar {calc}")