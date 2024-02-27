# x elevado a n
 
# Caso base: n = 0, x elevado a n

# Passo de recursão: x elevado a n = x * x elevado a n-1

def potencia(x, n):

    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)    


print(potencia(2, 1))     
