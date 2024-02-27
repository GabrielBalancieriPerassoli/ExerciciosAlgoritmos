#3) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do seu salário: "))
porcentagem = float(input("Quanto % aumentou seu salário: "))

calc = ((porcentagem / 100) * salario) + salario
print(f"\nSeu salario aumentou para {calc}")