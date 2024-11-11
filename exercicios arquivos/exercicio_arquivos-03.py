# Crie um programa que leia o conteúdo de um arquivo chamado artigo.txt e conte quantas vezes cada palavra aparece no texto. O programa deve exibir um relatório na tela, listando cada palavra acompanhada de sua respectiva contagem. Desconsidere diferenças de maiúsculas e minúsculas para a contagem e remova pontuações para evitar duplicidade de palavras.

def contar_letras():

    contador = {}

    try:
        arquivo = open("C:\\Users\\Tainara Marques\\Documents\\lab\\exercicios arquivos\\artigo.txt", "r")
        
        for linha in arquivo:
            linha = linha.lower()
            
            for char in linha:
                if 'a' <= char <= 'z': 
                    if char in contador:
                        contador[char] += 1
                    else:
                        contador[char] = 1
        
        for letra in contador:
            print(f"{letra}: {contador[letra]}")
    
    except FileNotFoundError:
        print("Erro: o arquivo não foi encontrado.")
    
    finally:
       arquivo.close()

contar_letras()
