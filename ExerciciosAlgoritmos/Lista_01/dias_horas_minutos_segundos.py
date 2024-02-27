#2) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

total_segundos = segundos + minutos * 60 + horas * 3600 + dias * 86400
print(total_segundos)

