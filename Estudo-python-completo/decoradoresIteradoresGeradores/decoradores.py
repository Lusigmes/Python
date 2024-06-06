# decoradores
def dizer_oi(nome):
    return f"Olá {nome}"

def vamos_la(nome):
    return f"{nome} vamos para a faculdade que horas?"

def nomear(funcao_nome, nome):
    return funcao_nome(nome)

print(nomear(dizer_oi, "miuzinho"))
print(nomear(vamos_la, "robertinho"))
print("*"*50)
