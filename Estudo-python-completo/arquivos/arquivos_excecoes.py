from pathlib import Path

try:
    arquivo = open("arquivo.txt", 'r')
except FileNotFoundError as e:
    print(f"Arquivo nao encontrado: {e}\n")
    
ROOT_PATH = Path(__file__).parent

try:
    diretorio = open(ROOT_PATH / "diretorio")
except Exception as e:
    print(f"Diretorio nao encontrado: {e}\n")
    

try:
    file = open("arq.txt", "r", encoding="utf-8")
except IOError as e:
    print(f"Erro: {e}\n")
except FileNotFoundError as e:
    print(f"Erro: {e}\n")
except UnicodeDecodeError as e:
    print(f"Erro: {e}\n")
except IsADirectoryError as e:
    print(f"Erro: {e}\n")