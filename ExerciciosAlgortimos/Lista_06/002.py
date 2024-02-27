n = int(input("Digite o valor de n: "))

contador = 0

if n > 0:    
    for numero in range(1, n * 2, 2):
        print(numero, end=" ")
        contador += 1
        if contador == n:
                break
else:       
    print("O valor deve ser maior que zero.")
        