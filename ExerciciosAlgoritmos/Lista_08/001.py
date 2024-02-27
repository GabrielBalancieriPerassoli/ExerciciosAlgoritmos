a = float(input("Digite o valor de A: "))

if a != 0:
    
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    
    delta = (b * b) - (4 * a * c)
    
    if delta < 0:
        
        print(f"O delta {delta} é negativo. Equação não possui raízes reais.")
        
    elif delta > 0:
        
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        
        print(f"\nValor de x1: {x1}, Valor de x2: {x2}")
        
    elif delta == 0:
        
        x = (-b) / (2 * a)
        
        print(f"O valor é {x}")
else:
    print("Não é possivel calcular está expressão devido ao valor 0 no A!")