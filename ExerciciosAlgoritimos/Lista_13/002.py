#2) Uma função importante na segurança da informação é a técnica de criptografia (ou cifragem).
# Um dos primeiros registros do uso de criptografia foi no Império Romano, pelo imperador César.

def cifra_cesar(texto, chave):

    resultado = ""

    for char in texto: # Itera sobre cada caractere no texto de entrada

        if char.isalpha(): # Verifica se o caractere é uma letra do alfabeto

            maiuscula = char.isupper() # Verifica se o caractere original era maiúsculo
            char = char.upper() # Transforma o caractere em maiúsculo para facilitar os cálculos
            codigo = ord(char) - ord('A') # Calcula o deslocamento do caractere atual
            novo_codigo = (codigo + chave) % 26 # Aplica a cifra de César com a chave especificada
            novo_char = chr(ord('A') + novo_codigo) # Converte o código resultante de volta para um caractere

            if not maiuscula: # Se o caractere original era minúsculo, converte de volta para minúsculo

                novo_char = novo_char.lower()

            resultado += novo_char # Adiciona o caractere cifrado ao resultado
        else:

            resultado += char # Se o caractere não for uma letra, mantém inalterado no resultado

    return resultado

def executar():

    while True:

        frase = input("\nDigite uma frase: ")
        chave_fixa = 3
        chave_variavel = int(input("Digite um valor de chave (1 a 50): "))

        if chave_variavel < 1 or chave_variavel > 50:

            print("\nChave fora do intervalo permitido.")
            continue
        
        cifra_fixa = cifra_cesar(frase, chave_fixa)
        cifra_variavel = cifra_cesar(frase, chave_variavel)

        print(f"\nCifra com chave fixa ({chave_fixa}): {cifra_fixa}")
        print(f"Cifra com chave variável ({chave_variavel}): {cifra_variavel}")

        decifragem_variavel = cifra_cesar(cifra_variavel, -chave_variavel)
        print(f"Decifragem com chave variável: {decifragem_variavel}")

        repetir = input("\nDeseja executar novamente? (S/N): ")

        if repetir.lower() != 's':
            break

executar()
