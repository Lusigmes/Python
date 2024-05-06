def minha_funcao(**kwargs):
    print("Função chamada com os seguintes argumentos:")
    print(kwargs)  # Verifique se os argumentos estão corretos
    for chave, valor in kwargs.items():
        print(f"{chave} : {valor}")

minha_funcao(nome="Alice", idade=30, cidade="São Paulo")
