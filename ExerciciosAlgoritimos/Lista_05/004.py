lista = []

i = 0

while i < 5:
    
    n = int(input(f"Digite o {i + 1} número: "))
    lista.append(n)
    i += 1

menor = lista[0] # Inicia com o primeiro valor da lista.
maior = lista[0] # Inicia com o primeiro valor da lista.
i = 1  # Reinicia o índice para 1.

while i < 5:
    
    if lista[i] > maior:   # Verifica se o valor atual da lista é maior.
        maior = lista[i]  # Se for, atualiza maior com o valor atual.
    elif lista[i] < menor: # Verifica se o valor atual da lista é menor.
        menor = lista[i] # Se for, atualiza menor com o valor atual.
    i += 1

print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")


    
    