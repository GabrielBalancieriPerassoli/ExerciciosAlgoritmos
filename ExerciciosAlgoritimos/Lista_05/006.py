import math

valores = []

i = 0
while i < 10:
    n = float(input(f"Digite o {i + 1} valor: "))
    valores.append(n) 
    i += 1
    
soma = 0    
for valor in valores:
    soma = soma + valor

media = soma / len(valores)
print(f"\nA média é: {media}")

i = 0
soma_dp = 0
while i < 10:
    dp = valores[i] - media
    soma_dp = soma_dp + dp ** 2
    i += 1
    
desvio_padrao = math.sqrt(soma_dp / len(valores))
print(f"O desvio padrão é: {desvio_padrao}")
    

