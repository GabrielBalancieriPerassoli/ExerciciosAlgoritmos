salario_fun = float(input("Digite o seu salário: "))

if salario_fun > 1250:
    new_salario = (10 / 100) * salario_fun
    salario_fun = new_salario + salario_fun
    print(f"Novo aumento: {salario_fun}")
elif salario_fun <= 1250:
    new_salario = (15 / 100) * salario_fun
    salario_fun = new_salario + salario_fun
    print(f"Novo aumento: {salario_fun}")
