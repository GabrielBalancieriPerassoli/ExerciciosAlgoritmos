condicao = True
soma = 0

while condicao:
    
    n = int(input("Digite numeros inteiros: "))
    
    if n == 0:
        condicao = False
        print("Finalizado.")
        
    soma = soma + n    
    
print(f"A soma dos números: {soma}")    
        
        