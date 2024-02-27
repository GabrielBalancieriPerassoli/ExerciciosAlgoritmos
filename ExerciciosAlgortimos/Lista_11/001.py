# 1) Leia uma matriz 4x4, imprima a matriz e retorne a localização (linha e a coluna) do maior valor.

import numpy as np

matriz = np.empty((4, 4), dtype=int)
for i in range(0, 4):
    for j in range(0, 4):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}, {j + 1}]: "))

print("Matriz 4x4:")
for i in range(0, 4):
    for j in range(0, 4):
        print('%3d' % matriz[i][j], end='')
    print()

maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"O maior valor na matriz é {maior_valor}, está na posição [{linha_maior + 1}, {coluna_maior + 1}]")