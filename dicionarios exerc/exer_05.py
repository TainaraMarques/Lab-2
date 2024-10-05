def menu():
    print("\n\n=-=-= BEM-VINDO =-=-=\n\n")
    print("1- createContact")
    print("2- includePhone")
    print("3- deletePhone")
    print("4- deleteContact")
    print("5- getPhones")
    print("6- exitProgram\n")
    
    opc = int(input("Digite a opção: "))

    return opc

def createContact(contatos):
    nome = input("> Digite seu nome: ")
    contatos[nome] = []

    while True:
        celular = input("> Digite seu celular: ")
        
        if not celular:
            break
        else:
            contatos[nome].append(celular)


    return contatos[nome], (celular)

def includePhone(contatos):
    p = input("Digite o nome do contato a ser alterado: ")
    c = int(input("Digite o nome do telefone a ser alterado: "))

    if p in contatos:
        contatos[p] = c

    return contatos[p]

def deletePhone(contatos):
    print(contatos)
    chave = input("Digite o nome que deja deletar o número: ")
    if chave in contatos:
        numero = input("Digite o número que deseja deletar: ")
        if numero in contatos[chave]:
            contatos[chave].remove(numero)
            if not contatos[chave]: 
                del contatos[chave]
    
    print(contatos)

    return chave, contatos

def deleteContact(contatos):
    print(contatos)
    chave = input("Digite o nome do contatos para deletar: ")
    if chave in contatos:
        del contatos[chave]



def getPhones(contatos):
    for nome in contatos:
        print("\n<<-- Contatos -->>> \n")
        print (contatos)

def main():
    contatos = {}
    opc = 0
    ad = 0
    get = 0 
    inc = 0
    delt = 0
    while opc != '6':
        opc = menu()
        if opc == 1: 
            ad = createContact(contatos)

        elif opc == 2:
            inc = includePhone(contatos)

        elif opc == 3:
            delt = deletePhone(contatos)

        elif opc == 4:
            delc = deleteContact(contatos)

        elif opc == 5:
            get = getPhones(contatos)

        else:
            break
    
main()