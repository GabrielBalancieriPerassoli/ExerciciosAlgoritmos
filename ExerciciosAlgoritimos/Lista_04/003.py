condicao = True
i = 0
soma = 0

while condicao:
    n = int(input("Digite um número inteiro (0 para finalizar): "))
    
    if n == 0:
        print("\n\nPrograma Finalizado.")
        condicao = False
        
    else:
        soma += n
        i += 1

media = soma / i
print(f"A média dos números inseridos é: {media}")