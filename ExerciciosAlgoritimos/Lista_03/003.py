distancia = float(input("Digite a distância da viagem em km: "))

if distancia < 0:
    print("A distância não pode ser negativa.")
else:
    km_curto = 0.50
    km_longo = 0.45

    if distancia <= 200:
        preco_passagem = distancia * km_curto
    else:
        preco_passagem = distancia * km_longo

    print(f"O preço da passagem é R$ {preco_passagem:.2f}")

