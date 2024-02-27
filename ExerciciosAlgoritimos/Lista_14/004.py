# 4) Calcule o máximo divisor comum (MDC) de dois números inteiros x e y.

# Caso base quando y == 0

def mdc(x, y):

    # Caso base: Se y for igual a 0, o MDC é x.
    if y == 0:
        return x
    else:
        # Chamada recursiva com os argumentos trocados (y, x % y).
        return mdc(y, x % y)

x = int(input("Digite um X: "))
y = int(input("Digite um Y: "))
resultado = mdc(x, y)
print(f"O MDC de {x} e {y} é {resultado}.")
