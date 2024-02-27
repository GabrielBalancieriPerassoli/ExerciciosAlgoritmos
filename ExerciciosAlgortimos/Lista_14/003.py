# 3) Determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2
# ocorre 3 vezes em 762021192.

# Caso base: quando N == 0, nao tem mais ultimo digito!

def qntVezes(n, k):
    
    if n == 0:
        return 0
    else:
            # Pega o ultimo digito do N
            ultimo_digito = n % 10

            # Verifica se o ultimo digito do N e igual a K
            if ultimo_digito == k:

                # Se for soma + 1, e passa por recursividade o numero menos o ultimo digito
                return 1 + qntVezes(n // 10, k)
            else:
                # Se não for igual, apenas chama a função recursivamente para o restante do número.
                return qntVezes(n // 10, k)


n = int(input("Digite qual o número você deseja: "))
k = int(input("Qual número deseja procurar em especifico: "))
print(qntVezes(n, k))