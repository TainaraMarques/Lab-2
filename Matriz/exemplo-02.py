def buscar_valor(matriz, valor):

    for linha in range(len(matriz)):
        #matriz[linha][coluna] -> isso vai armazenar o valor em questão!!
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == valor:
                numero_existe = True

    if numero_existe:
        print("o número esta presente na matriz")

    else:
        print("o número não esta presente na lista")

    
matriz = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

buscar_valor(matriz, 7)