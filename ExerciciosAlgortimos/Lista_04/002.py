deposito = float(input("Digite o valor do depósito inicial: "))
juros = float(input("Digite a taxa de juros em %: "))

saldo = deposito
ganho_juros = 0
i = 1

while i <= 24:
    
    juros_mes = deposito * (juros / 100)
    saldo += juros_mes
    ganho_juros += juros_mes
    
    print(f"Mês {i} - Saldo: R${saldo:.2f}")
    i += 1

print(f"\nTotal ganho com juros em 24 meses: R${ganho_juros}")