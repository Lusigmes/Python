import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent #opcional caso não ocorra problemas com caminho
print("root parent:", ROOT_PATH) 

## Comentando e descomentando de acordo com o teste de uso.

# os.mkdir(ROOT_PATH / "novo_dir_exemplo") # novo diretorio criado na raiz do projeto

# arquivo = open(ROOT_PATH / "arquivo_gerenciavel.txt", 'w', encoding="utf-8") # novo arquivo
# print(f"Arquivo: {arquivo.name} criado.")
# arquivo.close()

# os.rename("arquivo_gerenciavel.txt", "arquivo_renomeado.txt") #renomeia o arquivo
# print(f"Arquivo renomeado.")

# os.remove("arquivo_renomeado.txt") #remove o arquivo
# print(f"Arquivo removido.")

# shutil.move("arquivo_renomeado.txt", ROOT_PATH / "novo_dir_exemplo" / "arquivo_movido.txt") #move um arquivo qualquer para uma pasta escolhida, podendo renomea-lo(ou manter o mesmo nome)
# print(f"Arquivo movido e renomeado.")