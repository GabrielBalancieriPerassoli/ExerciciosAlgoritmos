lista = []

for i in range(5):
    
    n = int(input(f"Digite o {i + 1} número: "))
    lista.append(n)

menor = lista[0] # Inicia com o primeiro valor da lista.
maior = lista[0] # Inicia com o primeiro valor da lista.

for i in range(5):
    
    if lista[i] > maior:   # Verifica se o valor atual da lista é maior.
        maior = lista[i]  # Se for, atualiza maior com o valor atual.
    elif lista[i] < menor: # Verifica se o valor atual da lista é menor.
        menor = lista[i] # Se for, atualiza menor com o valor atual.

print(f"O maior número da lista é: {maior}")
print(f"O menor número da lista é: {menor}")
