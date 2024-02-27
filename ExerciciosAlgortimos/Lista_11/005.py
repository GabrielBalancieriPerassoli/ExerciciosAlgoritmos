# 5) Leia uma matriz de 3 x 3 elementos.
# a) Calcule a soma dos elementos que estão acima da diagonal principal.
# b) Calcule a soma dos elementos que estão abaixo da diagonal principal.
# c) Calcule a soma dos elementos que estão na diagonal principal.
# d) Calcule a soma dos elementos que estão na diagonal secundária.
# e) Calcule e imprima a sua transposta.

import numpy as np

matriz = np.empty((3, 3), dtype=int)

# Pergunta valor da matriz
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}, {j + 1}]: "))

sum_acima = 0
sum_abaixo = 0

# Calcular a soma dos elementos acima e abaixo da diagonal principal
for i in range(0, 3):
    for j in range(0, 3):

        if i < j:
            sum_acima += matriz[i, j]
        elif i > j:
            sum_abaixo += matriz[i, j]

print(matriz)
print(sum_acima)    
print(sum_abaixo)

# Calcular a soma dos elementos que estão na diagonal principal e secundária.

print(matriz)

sum_principal = 0
sum_secundaria = 0

for i in range(0, 3):
    for j in range(0, 3):

        if i == j:
            sum_principal += matriz[i, j]
        if i + j == 2:
            sum_secundaria += matriz[i, j]
            

print(sum_secundaria)
print(sum_secundaria)  

print(matriz)

# Calcular e imprimir a transposta da matriz
matriz_transposta = np.transpose(matriz)

print("Matriz Transposta:")
for i in range(3):
    for j in range(3):
        print(matriz_transposta[i, j], end=' ')
    print()

            
                


