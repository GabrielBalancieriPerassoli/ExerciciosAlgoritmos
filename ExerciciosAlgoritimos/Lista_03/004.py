kilowatt = int(input("Qual é a quantidade consumida kWh: "))

opcao = input(("R para residências, I para indústrias, C para comércios "))

if opcao == "R":

    if kilowatt <= 500:
        p_res = 0.40
        kilowatt = kilowatt * p_res
        print(kilowatt)
    elif kilowatt > 500:
        p_res = 0.65
        kilowatt = kilowatt * p_res
        print(kilowatt)

elif opcao == "I":

    if kilowatt <= 1000:
        p_res = 0.55
        kilowatt = kilowatt * p_res
        print(kilowatt)
    elif kilowatt > 1000:
        p_res = 0.60
        kilowatt = kilowatt * p_res
        print(kilowatt)

elif opcao == "C":

    if kilowatt <= 5000:
        p_res = 0.55
        kilowatt = kilowatt * p_res
        print(kilowatt)
    elif kilowatt > 5000:
        p_res = 0.60
        kilowatt = kilowatt * p_res
        print(kilowatt)
