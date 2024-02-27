# 6) Faça uma função que receba três números e retorne qual deles é o maior.

def maior(n1, n2, n3):
    
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n1:
        return n3
    else:
        return "Numeros iguais"


n1 = int(input("Digite o n1: "))
n2 = int(input("Digite o n2: "))
n3 = int(input("Digite o n3: "))

print(maior(n1, n2, n3))