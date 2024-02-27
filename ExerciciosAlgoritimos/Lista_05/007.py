valores = []

i = 0
while i < 6:
    n = int(input(f"Digite o {i + 1} valor: "))
    valores.append(n) 
    i += 1
    
soma_pares = 0    
len_impares = 0
for valor in valores:
    if valor % 2 == 0:
        soma_pares = soma_pares + valor
    elif valor % 2 != 0:
        len_impares += 1
        
    
print(f"\nSoma dos números pares: {soma_pares}")
print(f"\nQuantidade dos números impares: {len_impares}")
    

