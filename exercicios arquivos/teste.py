def listas():
    try:
        # Abrir os arquivos lista1.txt e lista2.txt em modo leitura
        with open("lista1.txt", "r") as list1, open("lista2.txt", "r") as list2:
            # Ler as linhas dos arquivos
            produtos_lista1 = list1.readlines()
            produtos_lista2 = list2.readlines()

            # Remover quebras de linha (\n) das listas
            produtos_lista1 = [produto.strip() for produto in produtos_lista1]
            produtos_lista2 = [produto.strip() for produto in produtos_lista2]

        # Comparar os produtos e escrever no arquivo diferenca.txt
        with open("diferenca.txt", "w") as lista3:
            for produto in produtos_lista1:
                if produto not in produtos_lista2:
                    lista3.write(produto + "\n")

    except FileNotFoundError:
        print("Erro: um ou ambos os arquivos não foram encontrados.")

# Chama a função
listas()
