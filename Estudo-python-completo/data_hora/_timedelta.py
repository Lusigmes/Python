import datetime
# from datetime import datetime, timedelta

tamanho_producao = 'G'
menor_tempo = 30
tempo_medio = 45
maior_tempo = 60
data_atual = datetime.datetime.now()

if tamanho_producao == "P":
    data_estimada = data_atual + datetime.timedelta(days=menor_tempo)# retorna um objeto timedelta
    print(f"Começamos a produção em: {data_atual} e "+
          f"estará pronto para entrega em {menor_tempo} dias, em: {data_estimada}")
    
elif tamanho_producao == "M":
    data_estimada = data_atual + datetime.timedelta(days=tempo_medio)# retorna um objeto timedelta
    print(f"Começamos a produção em: {data_atual} e "+ 
          f"estará pronto para entrega em {tempo_medio} dias, em: {data_estimada}")
    
else:
    data_estimada = data_atual + datetime.timedelta(days=maior_tempo)# retorna um objeto timedelta
    print(f"Começamos a produção em: {data_atual} e "+
          f"estará pronto para entrega em {maior_tempo} dias, em: {data_estimada}")

print("*"*30)

# print(datetime.date.today() - datetime.timedelta(hours=4))

print(datetime.datetime(2000,1,1,22,38,1)) # mostra data 200-01-01 hora 22:38:01

hora_subtraida = datetime.datetime.now() - datetime.timedelta(hours=2) # mostra data atual e remove 2h # retorna um objeto timedelta
print(hora_subtraida.time()) # para manipular a hora, é necessario construir a data e extrair a hora
print(hora_subtraida.date()) # para manipular a data, é necessario construir a data e extrair a data