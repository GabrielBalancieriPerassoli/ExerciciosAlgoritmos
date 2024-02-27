n = int(input("Digite um N: "))

i = 2

primeiro = 1
segundo = 1

if n > 0:
    
    if n == 1:
        print(1)
    elif n >= 2:
        print(1)
        print(1)
        
    while i < n:
    
        soma = primeiro + segundo
        
        primeiro = segundo
        segundo = soma
        
        print(soma)
            
        i += 1
else:
    print("O número tem que ser maior que 0")