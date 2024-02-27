# 5) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa
# elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:
#   • Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
#   • Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição
#   em y.
#   • Diferença entre x e y: todos os elementos de x que não existam em y.
#   • Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.
#   • União entre x e y: todos os elementos de x, e todos os elementos de y que não
#   estão em x.

x = [] 
y = []

for i in range(5):
    numeroX = float(input(f"Digite o X{i + 1}: "))
    numeroY = float(input(f"Digite o Y{i + 1}: "))

    x.append(numeroX)
    y.append(numeroY)

# Função para calcular a soma entre x e y
def soma(x, y):

    soma = []

    for i in range(5):
        soma.append(x[i] + y[i])

    return soma

# Função para calcular o produto entre x e y
def produto(x, y):

    multiplicacao = []

    for i in range(5):
        multiplicacao.append(x[i] * y[i])

    return multiplicacao

# Mostrar a soma entre x e y
print("Soma entre x e y:")
print(soma(x, y))

# Mostrar o produto entre x e y
print("Produto entre x e y:")
print(produto(x, y))

# Mostrar a diferença entre x e y
print("Diferença entre x e y:")
for i in range(5):
    if x[i] != y[i]:
        print(x[i], end=' ')

# Mostrar a interseção entre x e y
print("\nInterseção entre x e y:")
for i in range(5):
    if x[i] == y[i]:
        print(x[i], end=' ')

# Mostrar a união entre x e y usando conjuntos
uniao = x

for elemento_y in y:
    if elemento_y not in uniao:
        uniao.append(elemento_y)

# Mostrar o vetor de união
print("\nUnião entre x e y: ")
print(uniao)
        
