import random

def gerar_cartela_bingo():
    numeros = random.sample(range(100), 25)

    # Converte a lista em uma matriz 5x5
    cartela = [numeros[i:i + 5] for i in range(0, 25, 5)]
    
    return cartela

def exibir_cartela(cartela):
    print("Cartela de Bingo:")
    for linha in cartela:
        print(" | ".join(map(str, linha)))  # Converte números para string e exibe

# Gera e exibe a cartela
cartela_bingo = gerar_cartela_bingo()
exibir_cartela(cartela_bingo)