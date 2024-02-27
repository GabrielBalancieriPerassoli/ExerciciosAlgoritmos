#Versão Iterativa

def fatorialI(n):

    total, k = 1, 1

    while k <= n:

        total = total * k
        k = k + 1

    return total

print(fatorialI(5))    

#Versão Recursiva

# EXEMPLO
# 5!
# 5 * 4!
#     4 * 3!
#         3 * 2!
#             2 * 1!

# Fatorial de 1 é 1 

def fatorial(n):
    
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)  

print(fatorial(5))







