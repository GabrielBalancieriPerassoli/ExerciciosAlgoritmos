n = int(input("Digite um número: "))
num_reserva = n

invertido = 0

while n > 0:
    
    ultimo_digito = n % 10 # Pega o ultimo digito, por ex 434, pega o 4
    n = n // 10 # Tira 1 número do valor inserido, por ex 434, fica 43
    invertido = (invertido * 10) + ultimo_digito # Armazena o digito do numero invertido

if num_reserva == invertido:
    print(f"\nNúmero digitado {num_reserva}")
    print(f"Número invertido {invertido}")
    print("Palindromo!")
else:
    print("\nEste número não é um Palindromo!")
        

