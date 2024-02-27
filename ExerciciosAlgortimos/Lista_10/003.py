# 3) Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na
# ordem inversa.

import numpy as np

vetor = []

for i in range(6):
    
    numero = int(input(f"Digite o {i+1}º número real: "))

    vetor.append(numero)

vetor_valor = np.array(vetor)

vetor_invertido = np.flip(vetor)

# Imprimir os valores invertidos
print("Valores na ordem inversa:")
for valor in vetor_invertido:
    print(valor)
    