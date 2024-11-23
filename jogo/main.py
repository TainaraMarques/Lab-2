from menu import menu
def main():
    opc = int(input("~~>> Escolha uma opção: "))
    while True:
        if opc == 1:
            import jogot

        elif opc == 2:
            import ver_score
    
        elif opc == 3:
            import meus_pontos

        elif opc == 4:
            print("==>> Obrigado por ter jogado! Saindo do sistema...")
            break
main()