# Implemente um programa que compare o conteúdo de dois arquivos, lista1.txt e lista2.txt, onde cada um contém uma lista de produtos, com um produto por linha. O programa deve gerar um novo arquivo chamado diferenca.txt, que deve conter apenas os produtos que estão presentes em lista1.txt, mas ausentes em lista2.txt. Essa lista resultante deve ser salva no novo arquivo, com um produto por linha.

def listas():
    list1 = open("C:\\Users\\Tainara Marques\\Documents\\lab\\exercicios arquivos\\lista1.txt", "r")
    list2 = open("C:\\Users\\Tainara Marques\\Documents\\lab\\exercicios arquivos\\lista2.txt", "r")

    read1 = list1.readlines()
    read2 = list2.readlines()
    lista3 = open("diferenca.txt", "w")

    for produtos in read1:
        if produtos not in read2:
            lista3.write(produtos)

listas()


