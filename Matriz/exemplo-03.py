def menor_valor(matriz):
    mv = matriz [0][0]
    for linha in range (len(matriz)):
        for coluna in range (len(matriz[linha])):
            if matriz[linha][coluna] < mv:
                mv = matriz[linha][coluna]
    return mv

matriz = [
    [65, 45, 95],
    [59, 58, 27],
    [19 , 26, 23],
    [89, 52, 31]
]

mv = menor_valor(matriz)

print ("O menor valor da matriz é", mv)