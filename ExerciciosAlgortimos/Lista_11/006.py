# 6) Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo.
# Sabendo que cada cartela deverá conter 5 linhas de 5 números, gere estes dados de modo a não ter
# números repetidos dentro das cartelas. O programa deve exibir na tela a cartela gerada.

import numpy as np

cartela = np.zeros((5, 5), dtype=int)

for i in range(5):
    for j in range(5):

        numero = np.random.randint(0, 99)
        
        while numero in cartela:
            numero = np.random.randint(0, 99)
        
        cartela[i, j] = numero

for linha in cartela:
    for numero in linha:
        print(numero, end=' ')
    print()


