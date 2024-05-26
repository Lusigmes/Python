import csv

try:
    with open("netflix_shows.csv", 'r', encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(linha) 
except IOError as e:
    print(f"Erro: {e}")    