quantidade = int(input("Qual foi a quantidade comprada de itens: "))
i = 0
condicao = True
soma = 0
while(i < quantidade):
    
    print("Códigos: 1 - 2 - 3 - 5 - 9")
    codigo = int(input("Digite o código do produto: "))

    if codigo == 1:
        valor = 0.50
    elif codigo == 2:
        valor = 1
    elif codigo == 3:
        valor = 4
    elif codigo == 5:
        valor = 7
    elif codigo == 9:
        valor = 8
    elif codigo == 0:
        print("Programa Encerrado.")
        quantidade = i
    else: 
        print("Código não encontrado!")
        
    if codigo != 0:    
        soma = soma + valor
        
    i += 1
    
print(f"\nO total da compra dos itens foi de R$ {soma}")
    