#O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça
#o programa que lê o valor de N e M e informa o número de combinações possíveis.

import math

def calcular_combinacoes(N, M):
    try:
        if M > N:
            raise ValueError("M deve ser menor ou igual a N.")
        if N < 0 or M < 0:
            raise ValueError("N e M devem ser números inteiros positivos.")
 
        combinacoes = math.factorial(N) // (math.factorial(M) * math.factorial(N - M))
        return combinacoes

    except ValueError as e:
        print(f"Erro: {e}")
        return None

try:
    N = int(input("Digite o número total de alunos (N): "))
    M = int(input("Digite o tamanho de um dos grupos (M): "))

    resultado = calcular_combinacoes(N, M)
    if resultado is not None:
        print(f"O número de combinações possíveis é: {resultado}")

except ValueError:
    print("Erro: Digite valores inteiros para N e M.")
