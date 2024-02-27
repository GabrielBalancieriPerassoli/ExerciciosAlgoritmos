disciplina1 = float(input("Digite a disciplina 1: "))
disciplina2 = float(input("Digite a disciplina 2: "))
disciplina3 = float(input("Digite a disciplina 3: "))

media = (disciplina1 + disciplina2 + disciplina3) / 3

if media >= 7 and media <= 10:
    print("Aprovado!")
elif media < 0 or media > 10:
    print("Nota inválida!")
else:
    print("Reprovado!")    