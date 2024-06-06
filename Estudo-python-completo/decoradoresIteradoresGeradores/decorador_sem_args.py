def decorador_teste(funcao):
    def email():
        print("Antes da ação do decorador")
        funcao()
        print("Apos a ação do decorador")
        
    return email

@decorador_teste #melhora a sintaxe, reduz a verbosidade
def mensagem():
    print("Esta mensagem é o conteúdo do email.")

# msg = decorador_teste(mensagem)
mensagem()

#*args e *kwargs