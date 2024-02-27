# 3) Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca desse valor
# na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de “não
# encontrado”.

import numpy as np

x = int(input("Digite um valor a ser encontrado: "))

matriz = np.empty((5, 5), dtype=int)

for i in range(0, 5):
    for j in range(0, 5):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}, {j + 1}]: "))

encontrado = False

for i in range(0, 5):
    for j in range(0, 5):
        if x == matriz[i][j]:
            print(f"Encontrei o número {x} na posição [{i + 1}, {j + 1}] da matriz.")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"\nNão encontrei o número {x} dentro da matriz.")
        
print(matriz)  