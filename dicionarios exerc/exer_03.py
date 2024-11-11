def media(nota_1, nota_2):
    return (nota_1 + nota_2) / 2

def main():
    dicionario = {}

    while True:
        nome = input("Insira seu nome (ou deixe em branco para sair): ")
        if not nome:
            break

        nota_1 = float(input("Insira a sua primeira nota: "))
        nota_2 = float(input("Insira a sua segunda nota: "))
        
        dicionario[nome] = [nota_1, nota_2]

    p = input("Digite o nome que você quer procurar: ")
    if p in dicionario:
        notas = dicionario[p]
        med = media(notas[0], notas[1])
        print(f"A média de {p} é: {med}")
    else:
        print("Aluno não encontrado.")

main()
