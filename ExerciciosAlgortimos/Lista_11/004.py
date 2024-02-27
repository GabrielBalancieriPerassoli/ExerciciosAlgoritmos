# 4) Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
# A[i][j] = 2 elevado a i + 7 vezes j − 2 se i < j;
# A[i][j] = 3 vezes i elevado a 2 − 1 se i = j;
# A[i][j] = 4 vezes i elevado a 3 − 5 vezes j elevado 2 + 1 se i > j.

import numpy as np

matriz = np.empty((10, 10), dtype=int)

for i in range(10):
    for j in range(10):
        if i < j:
            matriz[i][j] = 2**i + 7 * j - 2
        elif i == j:
            matriz[i][j] = 3 * i**2 - 1
        elif i > j:
            matriz[i][j] = 4 * i**3 - 5 * j**2 + 1

print("Matriz: ", matriz)