#5) Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Qual é a distância a percorrer: "))
velocidade_media = float(input("Qual é a velocidade média: "))

calc = distancia / velocidade_media
tempo = int(calc)
minutos = (calc - tempo) * 60
print(f"O tempo em horas é de {tempo} e o tempo em minutos é de {minutos:.0f}")
