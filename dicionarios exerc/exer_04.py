def vogais():
    v = {}

    frase = input("Digite uma frase: ")
    frase = frase.lower()
    
    for letra in frase:
        v[letra] = v.get(letra,0) + 1
    print(frase, "-->>", v)

vogais()