from menu import menu
from saldo import ler_saldo
from sacar import sacar
from depositar import deposito
from extrato import ver_extrato

def main():
    opc = ''
    while opc != '5':
        m = menu()
        opc = input("\n-> Ecolha uma das opções: ")

        if opc == '1':
            valor_saque = float(input("Digite o valor desejado para o saque: "))
            resultado_saque = sacar(valor_saque)
            print(resultado_saque) 

        elif opc == '2':
            valor_deposito = float(input("Digite o valor desejado para o depósito: "))
            resultado_deposito = deposito(valor_deposito)
            print(resultado_deposito) 

        elif opc == '3':
            saldo = ler_saldo()
            print(f"Seu saldo atual é: R${saldo:.2f}")

        elif opc == '4':
            extrato = ver_extrato()
            print("Extrato:\n", extrato) 

        elif opc == '5':
            print("Saindo do sistema...")

        else:
            print("Opção inválida, tente novamente.")  
            
main()
