def vogais():
    v = {}
    vogais = ["a","e","i","o","u"]

    frase = input("Digite uma frase: ")
    frase = frase.lower()
    
    for letra in frase:
        if letra in vogais:
            v[letra] = v.get(letra,0) + 1
    print(v)

vogais()