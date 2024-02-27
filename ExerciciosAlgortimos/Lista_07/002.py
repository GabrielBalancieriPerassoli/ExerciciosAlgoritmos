lista = [3, 6, 7, 9, 10, 11, 13, 15, 20, 1, 0, 4]

n = int(input("Digite o número que está procurando: "))
condicao = True

for i in range(len(lista)):
    
    if lista[i] == n:
        print(f"Achei na posição {i}!")
        condicao = False
        
if condicao:
    print("Não achei!")
            