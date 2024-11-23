import random
def jogo():    
    matriz = [
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"]
]
    

    nome = input("\n\nDigite seu nome: ")
    if not nome:
        print("Por favor digite um nome válido!!")
        return jogo()

    else:
        visivel = [
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"],
            ["⬜","⬜","⬜","⬜","⬜","⬜","⬜"]
]
        posicoes_bombas = random.sample(range(7 * 7),20)
        for posicao in posicoes_bombas:
            linha = posicao // 7   
            coluna = posicao % 7   
            matriz[linha][coluna] = "💣"
        pontos = 0

        while True:
            print("   " + "    ".join(str(i) for i in range(len(visivel[0]))))
            print("  " + "---" * (len(visivel[0]) * 2)) 
            i = 0
            for linha in visivel:
                print(f"{i} " + " | ".join(linha))
                i += 1
         
            try:
                x = int(input("\nDigite a linha (0 a 5): "))
                y = int(input("Digite a coluna (0 a 5): "))

                if x < len(visivel) and y < len(visivel[0]):
                    visivel[x][y] = matriz[x][y]
                    if matriz[x][y] == "⬜":
                        print("\n\nSeguro\n")
                        pontos += 1
                    if pontos == 28:
                        print("--->>> Parabens!! Voçê conseguiu achar todas as casas seguras sem encontrar nenhuma bomba")
                        score = open("pontuacao.txt", "a")
                        score.write(f"{nome} {pontos}\n")
                        break
                        
                    elif matriz[x][y] == "💣":
                        print("   " + "    ".join(str(i) for i in range(len(matriz[0]))))
                        print("  " + "---" * (len(matriz[0]) * 2)) 
                        i = 0
                        for linha in matriz:
                            print(f"{i} " + " | ".join(linha))
                            i += 1

                        print("\n\n~~> você perdeu ao encontrar a bomba!!\n ")
                        print("Jogo encerrado. Obrigado por jogar!\n\n")
                        score = open("pontuacao.txt", "a")
                        score.write(f"{nome} {pontos}\n")
                        break

                        
                        
        
                else:
                    print("\n\n-->> Coordenadas fora do intervalo. Tente novamente.\n\n")

            except ValueError:
                print("\n\nPor favor, insira números válidos.\n")

jogo()
