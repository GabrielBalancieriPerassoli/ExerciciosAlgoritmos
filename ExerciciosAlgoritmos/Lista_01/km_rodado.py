#7) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input("Quantos Km você percorreu? "))
dias = int(input("Por quantos dias você alugou o carro? "))

diaria = 60
km_rodado =  0.15

calc = (km * km_rodado) + (dias * diaria)
print(f"\nO preço total a pagar é: R$ {calc:.2f}")

