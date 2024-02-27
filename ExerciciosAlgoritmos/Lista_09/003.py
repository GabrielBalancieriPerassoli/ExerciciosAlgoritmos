# 3) Faça uma função que receba dois números e retorne qual deles é o maior.

def maior(n1, n2):

    if n1 > n2:
        return n1
    else:
        return n2


n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))

print(maior(n1, n2))