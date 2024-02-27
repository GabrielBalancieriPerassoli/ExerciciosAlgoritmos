# 2) Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos.
# Escreva ao final a matriz obtida.

import numpy as np

matriz = np.zeros((5, 5), dtype=int)

print("Matriz 5x5:")

for i in range(5):
    
    matriz[i][i] = 1
    
    for j in range(5):
        
        print(matriz[i][j], end=' ')
    print()