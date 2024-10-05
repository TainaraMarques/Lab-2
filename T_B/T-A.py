def menu():
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Visualizar produtos")
    print("4 - Vender produto")
    print("5 - Relatórios de venda")
    print("6 - Sair")

    opc = int(input("Digite uma opção: "))

    return opc
    

def adicionar(estoque):
        produto = input("Adicione um produto na lista: ")
        quantidade = int(input("Informe a quantidade do produto: "))
        preco = float(input("Informe o preço do produto: "))
        estoque[produto ] = {
            'quantidade': quantidade,
        'preco': preco
        }

        return estoque,quantidade

def buscar(estoque):
    print(estoque.keys())
    chave = input("Digite o nome do produto para buscar: ")
    if chave in estoque:
        print(estoque.get(chave))
        

    else:
        print("O produto não esta na lista! Volte ao menu e adicione o produto. ")

def listar(estoque):
    for chave in estoque:
        print (estoque)

def vender(estoque,vendas):
    venda = input("Digite o nome do produto vendido: ")
    qtd_vendida = int(input("Digite a quantidade vendida: "))
    preco = estoque[venda]['preco']
    vt  =  preco * qtd_vendida
    if venda in estoque:
        quantidade_atual = estoque[venda]['quantidade']
        
        if qtd_vendida <= quantidade_atual:
            quantidade_atual -= qtd_vendida 
            estoque[venda]['quantidade'] = quantidade_atual 

            print(f"Quantidade restante em estoque: {quantidade_atual}")
            print(f"{vt} é o valor total da venda")
            vendas.append({'nome': venda, 'quantidade': qtd_vendida, 'valor': vt})
        else:
            print("Quantidade vendida excede o estoque disponível")
    else:
        print(f"Produto '{venda}' não encontrado no estoque")
    
    
    
    return quantidade_atual, vt


def relatorioVendas(vendas):
    if vendas:
        print("\nRelatório de Vendas:")
        for venda in vendas:
            print(f"Produto: {venda['nome']}, Quantidade Vendida: {venda['quantidade']}, Valor Total: R${venda['valor']: }")
    else:
        print("Nenhuma venda realizada.")

def main():
    estoque = {
    }

    vendas = []

    opc = 0

    while opc != 5:
        opc = menu()
        if opc == 1:
            ad = adicionar(estoque)

        elif opc == 2:
            b = buscar(estoque)
            

        elif opc == 3:
            l = listar(estoque)

        elif opc == 4:
            v = vender(estoque,vendas)

        elif opc == 5:
            r = relatorioVendas(vendas)
        else:
            print ("Saindo do programa!!")
            
main()