extrato = [] 

def registrar_extrato(mensagem):
    extrato.append(mensagem)

def ver_extrato():
    if extrato:
        return "\n".join(extrato)
    else:
        return "Nenhuma transação registrada."
