import datetime

def registrar_movimentacao(tipo, valor, conta):
    # Registra a movimentação com a data e hora
    movimentacao = {
        "tipo": tipo,
        "valor": valor,
        "data": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    conta["movimentacoes"].append(movimentacao)

def depositar(valor, conta):
    if valor > 0:
        conta["saldo"] += valor
        registrar_movimentacao("Depósito", valor, conta)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do depósito deve ser positivo.")

def sacar(valor, conta):
    if valor > conta["saldo"]:
        print("Erro: Saldo insuficiente para essa transação.")
    elif valor > conta["transaction_limit"]:
        print(f"Erro: O valor de saque excede o limite de R${conta['transaction_limit']:.2f} por transação.")
    elif valor > 0:
        conta["saldo"] -= valor
        registrar_movimentacao("Saque", valor, conta)
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Erro: O valor do saque deve ser positivo.")

def verificar_saldo(conta):
    print(f"Saldo atual: R${conta['saldo']:.2f}")

def exibir_historico(conta):
    if conta["movimentacoes"]:
        print("Histórico de movimentações:")
        for mov in conta["movimentacoes"]:
            print(f"{mov['data']} - {mov['tipo']}: R${mov['valor']:.2f}")
    else:
        print("Nenhuma movimentação registrada.")

def main():
    conta = {
        "saldo": 0.0,
        "transaction_limit": 1000.0,  # Limite de saque por transação
        "movimentacoes": []
    }
    
    while True:
        print("\n<<--- Caixa Eletrônico --->>\n")
        print("1. Depositar dinheiro")
        print("2. Sacar dinheiro")
        print("3. Verificar saldo bancário")
        print("4. Histórico de movimentações")
        print("5. Sair")
        
        opcao = input("\n-> Escolha uma opção: ")

        if opcao == '1':
            try:
                valor = float(input("Digite o valor para depósito: R$"))
                depositar(valor, conta)
            except ValueError:
                print("Erro: Valor inválido. Por favor, digite um número.")
        elif opcao == '2':
            try:
                valor = float(input("Digite o valor para saque: R$"))
                sacar(valor, conta)
            except ValueError:
                print("Erro: Valor inválido. Por favor, digite um número.")
        elif opcao == '3':
            verificar_saldo(conta)
        elif opcao == '4':
            exibir_historico(conta)
        elif opcao == '5':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
