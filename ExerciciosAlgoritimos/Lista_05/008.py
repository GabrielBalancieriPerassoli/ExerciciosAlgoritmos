valores = []

while len(valores) < 10:
    n = int(input(f"Digite o {len(valores) + 1} valor: "))
    if n in valores:
        print("O valor ja existe na lsita. Digite o valor novamente: ")
    else:
        valores.append(n) 

print("\nValores inseridos:", valores)





