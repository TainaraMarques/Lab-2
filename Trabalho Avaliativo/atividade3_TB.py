def transposicao():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    matriz_transposta = []
    
    for coluna in range(len(matriz[0])):  
        nova_linha = [] 
        for linha in range(len(matriz)):  
            nova_linha.append(matriz[linha][coluna]) 
        matriz_transposta.append(nova_linha) 

    print("Matriz Original:")
    for linha in matriz:
        print(linha)

    print("\nMatriz Transposta:")
    for linha in matriz_transposta:
        print(linha)

transposicao()

