# 2) Calcule a soma de todos os valores de uma lista de números.

# Caso base: Lista vazia? soma = 0

# Passo de recursão:
# [ ,  ,  ,  ,   ,] 
#  lista[n - 1] + soma dos demais elementos - 1

def somaLista(lista, elementos):

    if elementos == 0:
        return 0
    else:
        return lista[elementos - 1] + somaLista(lista, elementos - 1)

lista = [1, 3, 5, 7, 9]
elementos = len(lista)

print(somaLista(lista, elementos))