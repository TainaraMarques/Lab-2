#Crie um programa que receba através de um input o valor numérico de um mês e retorne seu 
# valor escrito. Lembre de tratar as exceções do seu programa. Exemplo: 1 -> Janeiro, 12 -> Dezembro
def get_month_name(dictionary):
    try:
        number = int(input("Digite o número do mês (1 a 12): "))
        if number in dictionary:
            return dictionary[number]
        else:
            print("Esse mês não existe. Por favor, escreva um número entre 1 e 12.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return None

def main():
    dictionary = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    
    while True:
        month_name = get_month_name(dictionary)
        if month_name:
            print(f"O mês é: {month_name}")
            break

main()
