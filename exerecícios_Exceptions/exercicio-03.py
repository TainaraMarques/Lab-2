#Crie uma função que recebe um ano através de um input e defina se o mesmo é bissexto ou não. Utilize as seguintes
#regras: Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400. Exemplo: 1988 é bissexto pois
#é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível por 400.

def eh_bissexto(ano):
    try:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False
    except ValueError:
        # Exceção para quando a entrada não é um número inteiro
        print("Erro: O valor inserido não é um número inteiro. Digite um ano válido.")
        return None

ano = int(input("Digite um ano: "))

if eh_bissexto(ano) is not None:
    if eh_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
