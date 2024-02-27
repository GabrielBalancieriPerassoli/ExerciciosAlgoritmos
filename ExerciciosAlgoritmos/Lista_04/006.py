n = int(input("Digite um número: "))

if n >= 1:
    
    numero = 1
    print("Números primos de 1 a", n, ":")
    
    while numero <= n:
        
        if numero >= 2:
            primo = True
            divisor = 2
            
            while divisor * divisor <= numero:
                
                if numero % divisor == 0:
                    primo = False
                divisor += 1
                
            if primo:
                print(numero, end=" ")
                
        numero += 1
else:
    print("Não é um número maior que 1")