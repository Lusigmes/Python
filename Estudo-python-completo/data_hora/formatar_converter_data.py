import datetime

#strftime (string format time) formatando data e hora
data_atual= datetime.datetime.now()
print("strftime:", data_atual.strftime("%d/%m/%Y (%H:%M)"))

#strptime (string parse time) converter strirng para objeto datetime
data_hora_str = "28_11_1997 05--55--30" #deve estar igual a mascara do formato a ser convertido
marcara_data_hora_ptbr = "%d_%m_%Y %H--%M--%S" #deve estar igual ao formato de data passado na string
print("strptime:", datetime.datetime.strptime(data_hora_str, marcara_data_hora_ptbr))