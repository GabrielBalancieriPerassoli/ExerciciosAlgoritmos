# 6) Escreva um programa que leia um número inteiro positivo n e em seguida imprima n
# linhas do chamado Triangulo de Pascal:

n = int(input("Digite um numero positivo: "))

if n > 0:
    linha_atual = [1]
    i = 0
    while i < n:
        
        j = 0
        
        while j < len(linha_atual):
            print(linha_atual[j], end=" ")
            j += 1
        print()
        
        nova_linha = [1]
        j = 1
        
        while j < len(linha_atual):
            nova_linha.append(linha_atual[j - 1] + linha_atual[j])
            j += 1
        nova_linha.append(1)
        linha_atual = nova_linha
        
        i += 1
    