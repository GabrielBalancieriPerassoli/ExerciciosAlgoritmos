velocidade = int(input("Digite a velocidade do carro: "))

limite_v = 80

multa = (velocidade - limite_v) * 5

if velocidade > limite_v: 
    print("Você foi multado!")
    print(f"Valor da multa {multa} R$")
elif multa < 0 or velocidade == limite_v:
    print("Você está dentro da velocidade!")