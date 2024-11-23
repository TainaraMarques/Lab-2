def ver_score():
    ver = open("pontuacao.txt", "r")
    try:
            pontuacoes = [
                (linha.split()[0], int(linha.split()[1])) 
                for linha in ver
                if linha.strip() and len(linha.split()) == 2
            ]

            pontuacoes.sort(key=lambda x: x[1], reverse=True)

            melhores = pontuacoes[:5]

            if melhores:
                ranking = "\n".join(
                f"{i+1}. {nome} - {pontuacao}" for i, (nome, pontuacao) in enumerate(melhores)
            )
                return f"==>> Este é o ranking das 5 melhores pontuações do jogo:\n{ranking}"
            else:
                return "Ainda não há pontuações registradas."

    except FileNotFoundError:
        return "O arquivo de pontuações não foi encontrado."

print(ver_score())



ver_score()