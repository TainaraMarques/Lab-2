from saldo import ler_saldo, atualizar_saldo
from extrato import registrar_extrato

def sacar(valor):
    saldo = ler_saldo()
    if valor > saldo:
        return "Saldo insuficiente para realizar o saque."
    elif valor > 0:
        novo_saldo = saldo - valor
        atualizar_saldo(novo_saldo)
        registrar_extrato(f"Saque: R${valor}")
        return f"Saque de R${valor} realizado com sucesso!"
    else:
        return "Valor de saque inválido."
