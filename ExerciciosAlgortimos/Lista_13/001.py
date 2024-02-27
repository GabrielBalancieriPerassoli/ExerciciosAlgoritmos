def imprimir_tabela_ascii():
    
    colunas = 6
    linha = 32
    ultima_linha = 47

    print("\nTabela ASCII - Caracteres Visíveis\n")

    for i in range(ultima_linha - linha + 1):

        linha_atual = linha
        linha = linha_atual + 1
        linha_str = ""

        for j in range(colunas):

            coluna_str = f"{linha_atual:3d}    {chr(linha_atual)}"

            if chr(linha_atual) == " ":

                coluna_str = f"{linha_atual:3d}    espaço"

            linha_str += coluna_str.ljust(15)
            linha_atual += 16

        print(linha_str)

    print()    

imprimir_tabela_ascii()
