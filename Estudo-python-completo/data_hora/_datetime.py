import datetime
#uso do date
data = datetime.date(1997,11,28)
print(data)
print(datetime.date.today())
#uso do datetime com argumentos (YY-MM-DD H-M-S)
data_hora = datetime.datetime(1997,11,28, 5,55)
print(data_hora)
#uso do datetime com argumentos (YY-MM-DD)
data_hora2 = datetime.datetime(1997,11,28)
print(data_hora2)
print(datetime.datetime.today())# constroi o objeto data
print(datetime.datetime.now())# traz o objeto com timezone setado
#uso do time com argumentos (HH-MM)
hora = datetime.time(5,55)
print(hora)




