# 7) Faça um programa que leia duas matrizes 2 x 2 com valores reais. Ofereça ao usuário um menu
# de opções:
# (a) somar as duas matrizes
# (b) subtrair a segunda matriz da primeira
# (c) adicionar uma constante às duas matrizes
# (d) imprimir as matrizes

import numpy as np

matriz = np.empty((2, 2), dtype=float)
matriz2 = np.empty((2, 2), dtype=float)

for i in range(0, 2):
    for j in range(0, 2):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i + 1}, {j + 1}] da primeira matriz: "))

for i in range(0, 2):
    for j in range(0, 2):
        matriz2[i][j] = int(input(f"Digite o valor da posição [{i + 1}, {j + 1}] da segunda matriz: "))


def somarMatriz(matriz, matriz2):
    nova_matriz = np.empty((2, 2), dtype=float)

    for i in range(0, 2):
        for j in range(0, 2):
            nova_matriz[i][j] = matriz[i][j] + matriz2[i][j]

    return nova_matriz

def subMatriz(matriz, matriz2):
    nova_matriz = np.empty((2, 2), dtype=float)

    for i in range(0, 2):
        for j in range(0, 2):
            nova_matriz[i][j] = matriz2[i][j] - matriz[i][j]

    return nova_matriz

def constanteMatriz(matriz, matriz2):
    constante = float(input("\nDigite a constante para adicionar às matrizes: "))

    matriz = matriz + constante
    matriz2 = matriz2 + constante

    return matriz, matriz2

print("\n=========================================================")
print("\n(a) somar as duas matrizes")
print("(b) subtrair a segunda matriz da primeira")
print("(c) adicionar uma constante às duas matrizes")
print("(d) imprimir matrizes")
resposta = input("Escolha uma opção: ").upper()
print("\n=========================================================\n")

if resposta == "A":
    
    result = somarMatriz(matriz, matriz2)

    for linha in result:
        for numero in linha:
            print(numero, end='\t')
        print()

elif resposta == "B":

    result = subMatriz(matriz, matriz2)

    for linha in result:
        for numero in linha:
            print(numero, end='\t')
        print()

elif resposta == "C":

    matriz, matriz2 = constanteMatriz(matriz, matriz2)

    print("\nMatriz 1 com a constante adicionada:\n")

    for linha in matriz:
        for numero in linha:
            print(numero, end='\t')
        print()

    print("\nMatriz 2 com a constante adicionada:\n")

    for linha in matriz2:
        for numero in linha:
            print(numero, end='\t')
        print()

elif resposta == "D":

    print("\nMatriz 1:\n")

    for linha in matriz:
        for numero in linha:
            print(numero, end='\t')
        print()

    print("\nMatriz 2:\n")

    for linha in matriz2:
        for numero in linha:
            print(numero, end='\t')
        print()