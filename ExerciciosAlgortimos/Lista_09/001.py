# 1) Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
# minutos e segundos, e os converta em segundos.

def convSeg(horas, minutos, segundos):

    horas = horas * 3600
    minutos = minutos * 60
    segundos = segundos

    somaSeg = horas + minutos + segundos

    return somaSeg

horas = int(input("Digite as horas: "))    
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

print(convSeg(horas, minutos, segundos))