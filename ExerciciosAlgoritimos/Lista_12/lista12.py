import imagens

# Abra a imagem "Pedestre.png"
im = imagens.Imagem('Pedestre.png')

# Obtém as dimensões da imagem
largura = im.largura
altura = im.altura

# Percorre a imagem pixel a pixel
for i in range(altura):
    for j in range(largura):
        r, g, b = im[i][j]

        # Verifica se o pixel atual está dentro do intervalo de cores próximas ao preto
        if (r >= 0 and r <= 100 and g >= 0 and g <= 100 and b >= 0 and b <= 100):

            # Define a cor do pixel com um verde qualquer.
            im[i][j] = (11, 158, 50)

im.mostrar()
