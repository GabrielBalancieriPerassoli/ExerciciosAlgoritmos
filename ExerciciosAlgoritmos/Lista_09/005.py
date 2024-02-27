# 5) Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
# vários sı́mbolos de igual (Ex: ========). A função recebe por parâmetro quantos sinais
# de igual serão mostrados.

def desenhaLinha(qnt):

    linha = qnt * '='
    return linha


qnt = int(input("Digite a quantidade de '=' desejado: "))
print(desenhaLinha(qnt))