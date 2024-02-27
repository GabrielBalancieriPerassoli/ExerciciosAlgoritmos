# 2) Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos
# cada. Imprimir todos os conjuntos.

import numpy as np

vetor_numeros = np.empty(10, dtype=float)
vetor_quadrados = np.empty(10, dtype=float)

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor_numeros[i] = numero
    quadrado = numero ** 2
    vetor_quadrados[i] = quadrado

print("Conjunto dos números:")
print(np.array2string(vetor_numeros, precision=6, suppress_small=True))

print("Conjunto do quadrado dos quadrados:")
print(np.array2string(vetor_quadrados, precision=6, suppress_small=True))
