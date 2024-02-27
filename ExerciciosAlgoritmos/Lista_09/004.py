# 4) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
# consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
# mensagem de acordo com a tabela abaixo:

def distL(km, litros):

    if litros <= 0:
        return "A quantidade de litros de gasolina deve ser maior que zero."

    consumo = km / litros

    if consumo < 8:
        return "Venda o Carro!"
    elif consumo >= 8 and consumo <= 12:
        return "Econômico!"
    elif consumo > 12:
        return "Super Econômico!"

km = float(input("Digite a distancia de KM percorrida: "))
litros = float(input("Digite a quantidade de litros consumidos: "))

consumo = distL(km, litros)
print(consumo)