from pathlib import Path

ROOT_PATH = Path(__file__).parent

# with garante que o arquivo será fechado ao sair do bloco, mesmo se houver exceção
# evita vazamento de recursos 
try:
    # with open(ROOT_PATH / "file.txt", "r", encoding="utf-8") as arquivo:
    with open(ROOT_PATH / "file_not_exist.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
    # 1 / 0
except IOError as e:
    print(f"Erro: {e}")
# print(arquivo.read()) # não é possivel ler pois o arquivo está fechado
# arquivo.close() # redundante e desnecessario