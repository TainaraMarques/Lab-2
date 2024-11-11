def multiplicar_matriz():
    matriz = [
        [2, 3, 6, 9, 5],
        [1, 4, 12, 10, 50],
        [41, 11, 13, 7, 8],
        [10, 0, 23, 19, 15],
        [2, 5, 16, 14, 21],
    ]

    produtos = {}

    # Multiplicação vertical
    v1 = matriz[0][0] * matriz[1][0] * matriz[2][0] * matriz[3][0] * matriz[4][0]
    v2 = matriz[0][1] * matriz[1][1] * matriz[2][1] * matriz[3][1] * matriz[4][1]
    v3 = matriz[0][2] * matriz[1][2] * matriz[2][2] * matriz[3][2] * matriz[4][2]
    v4 = matriz[0][3] * matriz[1][3] * matriz[2][3] * matriz[3][3] * matriz[4][3]
    v5 = matriz[0][4] * matriz[1][4] * matriz[2][4] * matriz[3][4] * matriz[4][4]

    produtos['v1'] = v1
    produtos['v2'] = v2
    produtos['v3'] = v3
    produtos['v4'] = v4
    produtos['v5'] = v5

    # Multiplicação horizontal
    h1 = matriz[0][0] * matriz[0][1] * matriz[0][2] * matriz[0][3] * matriz[0][4]
    h2 = matriz[1][0] * matriz[1][1] * matriz[1][2] * matriz[1][3] * matriz[1][4]
    h3 = matriz[2][0] * matriz[2][1] * matriz[2][2] * matriz[2][3] * matriz[2][4]
    h4 = matriz[3][0] * matriz[3][1] * matriz[3][2] * matriz[3][3] * matriz[3][4]
    h5 = matriz[4][0] * matriz[4][1] * matriz[4][2] * matriz[4][3] * matriz[4][4]

    produtos['h1'] = h1
    produtos['h2'] = h2
    produtos['h3'] = h3
    produtos['h4'] = h4
    produtos['h5'] = h5

    # Multiplicação diagonal
    d1 = matriz[0][0] * matriz[1][1] * matriz[2][2] * matriz[3][3] * matriz[4][4]  
    d2 = matriz[0][4] * matriz[1][3] * matriz[2][2] * matriz[3][1] * matriz[4][0]  

    produtos['d1'] = d1
    produtos['d2'] = d2

    maior_chave = max(produtos, key=produtos.get)
    maior_valor = produtos[maior_chave]

    print(f"O maior produto é {maior_valor}, encontrado em {maior_chave}.")

# Chama a função
multiplicar_matriz()
