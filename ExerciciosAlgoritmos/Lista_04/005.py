n = int(input("Digite um número: "))

if n < 2:
    print("Não é um número maior que 1")
    
elif n == 2:
    print("2 é um número primo.")
    
else:
    
    primo = True
    divisor = 3
    
    while divisor * divisor <= n and primo:
        if n % divisor == 0:
            primo = False
            
        divisor += 2
        
    if primo:
        print(n, "é um número primo.")
        
    else:
        print(n, "não é um número primo.")
