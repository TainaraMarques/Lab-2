# Desenvolva um programa que leia o conteúdo de um arquivo chamado texto.txt e conte o número total de palavras contidas nele. O programa deve exibir essa contagem para o usuário. Caso o arquivo texto.txt não exista, exiba uma mensagem de erro informando a ausência do arquivo e encerre o programa. Dica: use o método split() para separar as palavras em cada linha, considerando que elas são delimitadas por espaços.
def contador_palavras():
    contador = {}
    try:
        arquivo = open ("C:\\Users\\Tainara Marques\\Documents\\lab\\exercicios arquivos\\texto.txt", "r")

        for palavras in arquivo:
            palavras = palavras.split(" ")
            contador[palavras] += 1
        
        for letra in contador:
            print(f"{palavras}: {contador[palavras]}")
    
    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado.")

contador_palavras()