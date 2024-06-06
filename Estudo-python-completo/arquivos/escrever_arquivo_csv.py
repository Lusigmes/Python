import csv

# Criando e Escrevendo no arquivo.csv
try: 
    # Especificar parametro newline='' em open,
    # para o método writerow não escrever "\n" no final de cada linha
    with open("usuarios.csv", mode="w", encoding="utf-8", newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["ID","NOME","IDADE"])
        writer.writerow(["1","Luis","26"])
        writer.writerow(["2","Rayssa","21"])
        writer.writerow(["3","Miu","7"])
        writer.writerow(["4","Roberto","1"])
        writer.writerow(["5","Larissa","2"])
        print(f"Arquivo: {arquivo.name} criado e escrito")
except IOError as e:
    print(f"Erro: {e}")
    
# Lendo o arquivo.csv criado
try:
    with open("usuarios.csv", "r", encoding="utf-8", newline='') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(linha)
            # print(linha[0], linha[1])
except IOError as e:
    print(f"Erro: {e}")
    
print("*"*50)
# lendo arquivo.csv com outro formato de leitura
ID_COL = 0
NOME_COL = 1
IDADE_COL = 2
try:
    with open("usuarios.csv", "r", encoding="utf-8", newline='') as arquivo:
        reader = csv.reader(arquivo)
        for i, linha in enumerate(reader):
            if i == 0:
                continue
            print(f"ID: {linha[ID_COL]}")
            print(f"NOME: {linha[NOME_COL]}")
            print(f"IDADE: {linha[IDADE_COL]}")
except IOError as e:
    print(f"Erro: {e}")
    