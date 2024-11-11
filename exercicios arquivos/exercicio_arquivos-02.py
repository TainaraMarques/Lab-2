# Escreva um programa que solicite ao usuário um número inteiro x, representando a quantidade de números aleatórios a serem gerados. O programa deve então criar um arquivo chamado numeros.txt e gravar x númerosaleatórios no intervalo de 0 a 100, cada um em uma linha. Certifique-se de que o arquivo seja gerado com os números na quantidade e no intervalo especificados.


import random

def aleatorios():
    try:
        x = int(input("Digite a quantidade de números aleatórios a serem gerados: "))
        n = open("numeros.txt", "w")
        numerosA = []
        for i in range(x):
            numerosaleatorios = random.randint(0,100)
            numerosA.append(numerosaleatorios)
    
        numerosAL = str(numerosA)
        numramdons = numerosAL.replace (",","\n")
        n.write(numramdons)

    except ValueError:
        print("O valor inserido não é válido. ")

aleatorios()


    