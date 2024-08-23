def somavalores(matriz):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range (len(matriz[linha])):
            soma += matriz[linha][coluna]
    return soma

matriz = [
    [65, 45, 95],
    [59, 58, 27],
    [19 , 26, 23],
    [89, 52, 31]
]

soma =  somavalores(matriz)

print (soma)