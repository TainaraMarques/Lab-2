def menu():
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Alterar produto")
    print("4 - Listar produto")
    print("5 - Sair")

    opc = int(input("Digite uma opção: "))

    return opc
    

def adicionar(produtos):
        nome = input("Adicione um produto na lista: ")
        quantidade = int(input("Informe a quantidade do produto: "))

        produtos[nome] = quantidade
        return produtos[nome]

def remover_pdt(produtos):
    print(produtos)
    chave = input("Digite o nome do produto para remover: ")
    if chave in produtos:
        del produtos [chave]
        print(produtos)

    else:
        print("O produto não esta na lista! Volte ao menu e adicione o produto. ")

def alterar(produtos):
    p = input("digite o produto para alterar: ")
    if p in produtos:
        alterar = int(input("digite a quantidade à alterar: "))
        produtos[p] = alterar
        if alterar == 0:
            del produtos[p]
        print(produtos)
        print(produtos)
        
        return p, alterar
    else:
        print("O produto não está na lista")


def listar(produtos):
    for chave in produtos:
        print (produtos)


def main():
    produtos = {}
    opc = 0
    ad = 0
    r = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            ad = adicionar(produtos)

        elif opc == 2:
            r = remover_pdt(produtos)
            

        elif opc == 3:
            a = alterar(produtos)

        elif opc == 4:
            l = listar(produtos)

        elif opc == 5:
            print ("Saindo do programa!!")
main()
