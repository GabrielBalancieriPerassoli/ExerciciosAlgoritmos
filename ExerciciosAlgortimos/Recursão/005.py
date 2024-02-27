# Caso Base: Lista vazia, soma = 0

# Passo de recursão:
# [ ,  ,  ,  ,   ,] 
#  lista[n - 1] + soma dos demais elementos

def soma(lista, n):

    if n == 0:
        return 0
    else:
        return lista[n - 1] + soma(lista, n - 1)    


lista = [1, 2, 3, 4, 5]
n = len(lista)
print(soma(lista, n))  