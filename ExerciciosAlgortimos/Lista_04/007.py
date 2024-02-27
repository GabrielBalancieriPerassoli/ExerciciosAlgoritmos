n = float(input("Digite um N: "))
b = 2

p = (b + (n / b)) / 2
quadrado_p = p * p

while abs(n - quadrado_p) > 0.0001:
    b = p
    p = (b + (n / b)) / 2
    quadrado_p = p * p
    
print("A raiz quadrada aproximada de", n, "é:", p)
    
