d = {
    'A':20,
    'B':30,
    'C':40
}

chave = input("digite uma chave: ").upper()
if chave in d.keys():
    print("Verdadeiro")

else:
    print("Falso")