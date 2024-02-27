import math

valores = []

for i in range(10):
    n = float(input(f"Digite o {i + 1} valor: "))
    valores.append(n) 
    
soma = 0    
for valor in valores:
    soma = soma + valor

media = soma / len(valores)
print(f"\nA média é: {media}")

soma_dp = 0
for i in range(10):
    dp = valores[i] - media
    soma_dp = soma_dp + dp ** 2
    
desvio_padrao = math.sqrt(soma_dp / len(valores))
print(f"O desvio padrão é: {desvio_padrao}")