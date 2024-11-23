def meu_score():
    try:
        pontos = open("pontuacao.txt", "r")
        linhas = pontos.readlines()

        nome_procurado = input("~~>> Digite o nome que você deseja procurar: ").strip()

        pontuacoes = []

        for linha in linhas:
            dados = linha.strip().split()
            if len(dados) == 2 and dados[1].isdigit():
                nome = dados[0]
                pontos = int(dados[1])

                if nome == nome_procurado:
                    pontuacoes.append(pontos)

        if pontuacoes:
            return f"Pontuações para {nome_procurado}: {pontuacoes}"
        else:
            return f"Nome {nome_procurado} não encontrado no arquivo."

    except FileNotFoundError:
        return "O arquivo 'pontuacao.txt' não foi encontrado."

print(meu_score())
