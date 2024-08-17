def multiplicar_matriz(matriz_informada, numero_escalar):
    for linha in range(len(matriz_informada)):
        for coluna in range(len(matriz_informada[coluna])):
            matriz_informada[linha][coluna] = matriz_informada[linha][coluna] * numero_escalar

    return matriz_informada

matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

resultado = multiplicar_matriz(matriz, 2)

for linha in range(len(resultado)):
    for coluna in range(len(resultado[linha])):
        print(linha, coluna, resultado[linha][coluna])