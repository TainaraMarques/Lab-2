"""
    Descreva aqui os principais erros que você encontrou:
        1.  Na linha 29 para usar o item mais comprado está usando a função de menor(min) e deveria ser maior(max)
        2. ** vai fazer com que o valor seja um expoente e nao uma multiplicação o que não faria sentido nessa conta eu acho
        3. Na linha 15 tinha um espaço na quantidade
        4. O valor esta escrito errado porque o valor no dicionario etá como valor e no def esta tentando acessar como vlr.
        5. 
"""     

import pandas as pd

# Objetivo: calcular o total de itens comprados pelo CJ e o item mais comprado
def calcular_itens_totais(inventario_cj):
    total_itens = 0
    for inventario_cj in inventario_cj:
        total_itens = 0
        total_itens += inventario_cj['quantidade'] * inventario_cj['valor']
    return total_itens

# Função para encontrar o item mais comprado
def item_mais_comprado(inventario_cj):
    itens_comprados = {}
    for compra in inventario_cj: 
        item = compra['quantidade']
        if item in itens_comprados:
            itens_comprados[item] += compra['quantidade']
        else:
            itens_comprados[item] = compra['quantidade']
    
    # Encontrar o item com maior quantidade comprada
    mais_comprado = max(itens_comprados, key=itens_comprados.get)
    return mais_comprado

# Função para calcular a média de valor por item
def media_valor_por_item(inventario_cj):
    # Convertendo lista em dataframe 
    dataframe = pd.DataFrame(inventario_cj)
    
    # Agrupar os dados por 'Produto' e calcular a média dos preços
    media_precos = dataframe.groupby('item')['valor'].mean().reset_index()

    media_precos.columns = ['item', 'média']

    return media_precos.to_string(index=False)

def limpa_inventario(inventario_cj):
   #...
   return 

def add_itens_inventario(inventario_cj, item, quantidade, valor):
    #...
    return inventario_cj

# Dados do inventário
inventario_cj = [
    {"item": "Pistola", "quantidade": 4, "valor": 300.50},
    {"item": "SMG", "quantidade": 2, "valor": 1200.0},
    {"item": "Granada", "quantidade": 5, "valor": 150.0}
]

# Chamar as funções
print("Total de itens comprados: ", calcular_itens_totais(inventario_cj))   
print("Média de valor por item:\n", media_valor_por_item(inventario_cj))
print("Item mais comprado: ", item_mais_comprado(inventario_cj))

#Adicione mais itens ao inventário

#Limpe o inventário