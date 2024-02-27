# 7) Escreva uma função para determinar a quantidade de números primos abaixo de N.

def p_N(N):

    cont = 0
    for i in range(2, N + 1):

        primo = True

        for j in range(2, int(i ** 0.5) + 1):

            if i % j == 0:
                primo = False
                break

        if primo:
            cont += 1
            
    return cont

N = int(input("Digite um valor N: "))
resultado = p_N(N)
print(f"A quantidade de números primos abaixo de {N} é {resultado}.")