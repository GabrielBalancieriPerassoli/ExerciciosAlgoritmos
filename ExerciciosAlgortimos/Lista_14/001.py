# 1) Dados dois números inteiros x e n, calcule o valor de x

# x elevado a n
# Caso base: n = 0, x elevado a n

def calcValor(x, n):

    if n == 0:
        return 1
    else:
        return x * calcValor(x, n - 1)

x = int(input("Digite um número X: "))
n = int(input("Digite um N para ser elevado: "))            
print(calcValor(x, n))