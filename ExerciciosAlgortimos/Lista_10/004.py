# 4) Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade
# de números negativos e a soma dos números positivos desse vetor.

vetor = []
quantidade_negativos = 0
soma_positivos = 0

for i in range(10):
    
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor.append(numero)

for numero in vetor:
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos}") 