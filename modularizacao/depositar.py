from saldo import ler_saldo, atualizar_saldo
from extrato import registrar_extrato

def deposito(valor):
    saldo = ler_saldo()
    if valor > 0:
        novo_saldo = saldo + valor
        atualizar_saldo(novo_saldo)
        registrar_extrato(f"Depósito: R${valor}")
        return f"Depósito de R${valor} realizado com sucesso!"
    else:
        return "Valor de depósito inválido."
