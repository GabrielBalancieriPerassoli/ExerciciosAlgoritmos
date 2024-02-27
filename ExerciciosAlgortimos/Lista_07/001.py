lista = []
condicao = True
i = 0
soma = 0
while condicao:
    precipitacoes = float(input(f"Digite a precipitação do dia {i + 1}, [0] para sair: "))
    
    if precipitacoes > 0: 
        lista.append(precipitacoes)
        soma = soma + precipitacoes
        i += 1
    elif precipitacoes == 0:
        condicao = False
    else:
        print("\nIgnorando valor negativo...")
else:
    print("Sem chuvas")

if soma > 0 and i > 0:
    media = soma / len(lista)
    
    print(f"\nO valor da soma das precipitacoes é de {soma}! ")
    print(f"O total de números positivos é de {i}!")    
    print(f"A media do mês foi de {media}!")
    
    